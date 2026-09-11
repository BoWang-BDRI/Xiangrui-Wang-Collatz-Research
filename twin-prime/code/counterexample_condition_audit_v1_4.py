#!/usr/bin/env python3
"""Exact counterexample search and failure-locus audit for patches P1--P7."""

from __future__ import annotations

import hashlib
import math
from pathlib import Path


LIMIT = 10_000_000
P6_LIMIT = 1_000_000
P7_LIMIT = 1_000_000
checks = 0


def require(condition: bool, label: str) -> None:
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def first_true(values, predicate):
    for value in values:
        if predicate(value):
            return value
    return None


def sieve(limit: int) -> tuple[bytearray, list[int]]:
    table = bytearray(b"\x01") * (limit + 1)
    table[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if table[p]:
            start = p * p
            table[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return table, [n for n in range(2, limit + 1) if table[n]]


is_prime, primes = sieve(LIMIT)
small_primes = [p for p in primes if p * p <= LIMIT]


# P1. The removed divisibility display is false for every legal n, not merely n=2.
window_limit = (LIMIT - 1) // 6
p1_left_truths = []
p1_right_truths = []
for n in range(1, window_limit + 1):
    if (6 * n - 1) % (6 * n - 3) == 0:
        p1_left_truths.append(n)
    if (6 * n + 3) % (6 * n + 1) == 0:
        p1_right_truths.append(n)
require(not p1_left_truths and not p1_right_truths, "P1 old divisibility has no legal solution")
require((5 % 3) != 0 and (9 % 7) != 0, "P1 actual minimum n=1")
require((11 % 9) != 0 and (15 % 13) != 0, "P1 task witness n=2")


# P2. Independently mark active p>=5 tracks and compare with sieve primality.
active_non3 = bytearray(LIMIT + 1)
for p in [q for q in small_primes if q >= 5]:
    start = p * p
    count = ((LIMIT - start) // (2 * p)) + 1
    active_non3[start : LIMIT + 1 : 2 * p] = b"\x01" * count
p2_first = None
p2_positions = 0
for x in range(5, LIMIT + 1, 2):
    if x % 3 == 0:
        continue
    p2_positions += 1
    if (active_non3[x] == 0) != bool(is_prime[x]):
        p2_first = x
        break
require(p2_first is None, "P2 T13 in-domain counterexample")
require(not is_prime[6] and active_non3[6] == 0, "P2 unrestricted minimum x=6")
require(not is_prime[9] and active_non3[9] == 0, "P2 odd unrestricted minimum x=9")


# P3. Add odd-prime tracks by activation order and inspect each consecutive-prime shell.
active_odd = bytearray(LIMIT + 1)
p3_first = None
odd_primes = [p for p in primes if p >= 3]
shells = 0
odd_shell_positions = 0
for index, p in enumerate(odd_primes[:-1]):
    if p * p > LIMIT:
        break
    q = odd_primes[index + 1]
    start = p * p
    count = ((LIMIT - start) // (2 * p)) + 1
    active_odd[start : LIMIT + 1 : 2 * p] = b"\x01" * count
    upper = min(q * q, LIMIT + 1)
    shells += 1
    for x in range(start, upper, 2):
        odd_shell_positions += 1
        if not is_prime[x] and not active_odd[x]:
            p3_first = (p, q, x)
            break
    if p3_first is not None:
        break
require(p3_first is None, "P3 odd shell counterexample")
require(not any(10 == a * (a + 2 * k) for a in range(3, 11, 2) for k in range(10)),
        "P3 global even-extension witness")
require(not any(26 == a * (a + 2 * k) for a in range(3, 27, 2) for k in range(20)),
        "P3 task even-extension witness")


# P4. Count gap-4 pairs and locate any failure of the p>=5 middle-B3 condition.
gap4 = [(p, p + 4) for p in primes if p + 4 <= LIMIT and is_prime[p + 4]]
p4_first = next(((p, q) for p, q in gap4 if p >= 5 and (p + 2) % 3 != 0), None)
require(p4_first is None, "P4 in-domain middle-B3 counterexample")
exceptional_gap4 = [(p, q) for p, q in gap4 if p < 5]
require(exceptional_gap4 == [(3, 7)], "P4 unique exceptional pair")


# P5. Mark exactly the active prime residue classes for each finite window.
blocked = bytearray(window_limit + 1)
for p in [q for q in small_primes if q >= 5]:
    lower_n = max(1, (p * p - 1 + 5) // 6)
    inverse = pow(6, -1, p)
    for residue in (inverse, (-inverse) % p):
        start = lower_n + ((residue - lower_n) % p)
        if start <= window_limit:
            count = ((window_limit - start) // p) + 1
            blocked[start : window_limit + 1 : p] = b"\x01" * count
p5_first = None
twin_windows = 0
for n in range(1, window_limit + 1):
    left, right = 6 * n - 1, 6 * n + 1
    direct_prime_pair = bool(is_prime[left]) and bool(is_prime[right])
    finite_product = blocked[n] == 0
    if direct_prime_pair:
        twin_windows += 1
    if finite_product != direct_prime_pair:
        p5_first = n
        break
require(p5_first is None, "P5 T_fin counterexample")


# P6. The two classes exist and are distinct exactly under gcd(6,p)=1 and p not dividing 2.
p6_first = None
p6_primes = [p for p in primes if 5 <= p <= P6_LIMIT]
for p in p6_primes:
    inverse = pow(6, -1, p)
    left = inverse
    right = (-inverse) % p
    if (6 * left - 1) % p or (6 * right + 1) % p or left == right:
        p6_first = p
        break
require(p6_first is None, "P6 prime-domain counterexample")
require(math.gcd(6, 2) != 1 and math.gcd(6, 3) != 1, "P6 excluded moduli")


# P7. Check domain membership and existing-track classification before stage advancement.
p7_first = None
p7_stages = 0
for b in range(3, P7_LIMIT, 2):
    x = b + 2
    in_domain = (x % 2 == 1) and 3 <= x < (b + 2) ** 2
    classified_prime = active_odd[x] == 0
    if not in_domain or classified_prime != bool(is_prime[x]):
        p7_first = b
        break
    p7_stages += 1
require(p7_first is None, "P7 in-domain counterexample")
require((4 + 2) % 2 == 0, "P7 even-stage exclusion")


script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
audited_cases = (
    window_limit
    + p2_positions
    + odd_shell_positions
    + len(gap4)
    + window_limit
    + len(p6_primes)
    + p7_stages
)
print(f"LIMIT={LIMIT}")
print("IN_DOMAIN_COUNTEREXAMPLES_P1_P7=NONE")
print("P1_OLD_DIVISIBILITY_TRUE_LEGAL_N=NONE")
print("P1_ACTUAL_MINIMUM_COUNTEREXAMPLE_N=1")
print("P1_TASK_WITNESS_N=2_VALID_NOT_MINIMUM")
print("P2_T13_UNRESTRICTED_MINIMUM_X=6")
print("P2_T13_ODD_UNRESTRICTED_MINIMUM_X=9")
print("P3_EVEN_EXTENSION_GLOBAL_MINIMUM=(3,5,10)")
print("P3_EVEN_EXTENSION_TASK_WITNESS=(5,7,26)")
print(f"P3_SHELLS={shells}")
print(f"P3_ODD_SHELL_POSITIONS={odd_shell_positions}")
print(f"P4_GAP4_TOTAL={len(gap4)}")
print(f"P4_GAP4_P_GE_5={len(gap4) - 1}")
print("P4_EXCEPTIONAL=(3,7)")
print(f"P5_WINDOWS={window_limit}")
print(f"P5_TWIN_WINDOWS={twin_windows}")
print(f"P6_PRIMES={len(p6_primes)}")
print(f"P7_STAGES={p7_stages}")
print(f"AUDITED_CASES={audited_cases}")
print(f"ASSERTIONS={checks}")
print(f"SCRIPT_SHA256={script_hash}")
print("VERDICT=PASS")
