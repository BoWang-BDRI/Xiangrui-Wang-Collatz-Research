#!/usr/bin/env python3
"""Exact-integer regression audit for the v1.4 final revision."""

from __future__ import annotations

import hashlib
import math
from pathlib import Path


LIMIT = 1_000_000
checks = 0


def require(condition: bool, label: str) -> None:
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def prime_sieve(limit: int) -> tuple[bytearray, list[int]]:
    table = bytearray(b"\x01") * (limit + 1)
    table[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if table[p]:
            start = p * p
            table[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return table, [n for n in range(2, limit + 1) if table[n]]


is_prime, primes = prime_sieve(LIMIT)
odd_primes = [p for p in primes if p >= 5]


def active_support(x: int) -> list[int]:
    support: list[int] = []
    for p in odd_primes:
        if p * p > x:
            break
        if x % p == 0:
            support.append(p)
    return support


def in_track(a: int, x: int) -> bool:
    return x % 2 == 1 and x % a == 0 and a * a <= x


# P1: T7 uses an ordered tuple, not divisibility bars.
require(5 % 3 != 0 and 9 % 7 != 0, "P1 actual minimum counterexample n=1")
require(11 % 9 != 0 and 15 % 13 != 0, "P1 task witness n=2")
for n in range(1, 100_001):
    boundary_left, left, right, boundary_right = 6 * n - 3, 6 * n - 1, 6 * n + 1, 6 * n + 3
    require(boundary_left % 3 == 0 and boundary_right % 3 == 0, f"P1 boundary n={n}")
    require(left % 6 == 5 and right % 6 == 1, f"P1 interior n={n}")


# P2: prime factor support is nonempty for a prime, but active support is empty.
require([p for p in odd_primes if 29 % p == 0] == [29], "P2 F(29)")
require(active_support(29) == [], "P2 A(29)")
for x in range(5, LIMIT + 1, 2):
    if x % 3 == 0:
        continue
    require((len(active_support(x)) == 0) == bool(is_prime[x]), f"P2 T13 x={x}")


# P3: square shells contain odd positions only and have already-active composite sources.
require(26 not in range(25, 49, 2), "P3 even witness exclusion")
small_primes = [p for p in primes if 3 <= p <= 1000]
for p, q in zip(small_primes, small_primes[1:]):
    for x in range(p * p, q * q, 2):
        if is_prime[x]:
            continue
        least = next(r for r in primes if x % r == 0)
        require(least <= p and in_track(least, x), f"P3 shell p={p},q={q},x={x}")


# P4: the exceptional (3,7) pair is separated from the p>=5 B3 statistic.
gap4 = [(p, p + 4) for p in primes if p + 4 <= LIMIT and is_prime[p + 4]]
require(len(gap4) == 8_144, "P4 total gap-4 count")
require(gap4[0] == (3, 7), "P4 exceptional first pair")
ordinary_gap4 = [(p, q) for p, q in gap4 if p >= 5]
require(len(ordinary_gap4) == 8_143, "P4 ordinary gap-4 count")
for p, q in ordinary_gap4:
    require((p + 2) % 3 == 0, f"P4 B3 middle p={p}")


# P5: direct finite product agrees with independent primality on every window to 10^6.
def t_fin(n: int) -> int:
    left, right = 6 * n - 1, 6 * n + 1
    for p in odd_primes:
        if p * p > right:
            break
        if left % p == 0 or right % p == 0:
            return 0
    return 1


window_limit = (LIMIT - 1) // 6
for n in range(1, window_limit + 1):
    left, right = 6 * n - 1, 6 * n + 1
    expected = int(bool(is_prime[left]) and bool(is_prime[right]))
    require(t_fin(n) == expected, f"P5 T_fin n={n}")


# P6: exactly two interrupted residue classes modulo every audited prime.
for p in [q for q in odd_primes if q <= 10_000]:
    inv6 = pow(6, -1, p)
    blocked = []
    for n in range(p):
        left_hit = (6 * n - 1) % p == 0
        right_hit = (6 * n + 1) % p == 0
        require(left_hit == (n == inv6), f"P6 left p={p},n={n}")
        require(right_hit == (n == (-inv6) % p), f"P6 right p={p},n={n}")
        if left_hit or right_hit:
            blocked.append(n)
    require(len(blocked) == 2 and p - len(blocked) == p - 2, f"P6 class count p={p}")


# P7: the next odd base is classified inside the current finite stage.
for b in range(3, 10_002, 2):
    x = b + 2
    require(3 <= x < (b + 2) ** 2, f"P7 domain membership b={b}")
    if is_prime[x]:
        occupied = False
    else:
        least = next(p for p in primes if x % p == 0)
        occupied = least <= b and in_track(least, x)
    require(occupied == (not bool(is_prime[x])), f"P7 stage classification b={b}")


script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
print(f"LIMIT={LIMIT}")
print(f"P4_GAP4_TOTAL={len(gap4)}")
print(f"P4_GAP4_P_GE_5={len(ordinary_gap4)}")
print(f"P5_WINDOWS={window_limit}")
print(f"ASSERTIONS={checks}")
print(f"SCRIPT_SHA256={script_hash}")
print("VERDICT=PASS")
