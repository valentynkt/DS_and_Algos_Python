# Hash Mastery Journey: From First Principles to Blockchain

> A comprehensive learning path for deeply understanding hashing - from mathematical foundations to implementing SHA-256 and blockchain primitives.

---

## Philosophy of This Journey

**Goal**: Not just to implement hash tables and SHA-256, but to understand _why_ they work, _why_ they're designed the way they are, and _what_ can go wrong.

**Approach**:

- Theory before implementation
- Understand the problem before the solution
- Know the failure modes and attacks
- Build everything yourself

**Time Estimate**: 2-3 weeks for deep understanding (not 1 week)

---

## Table of Contents

1. [Part I: Mathematical Foundations](#part-i-mathematical-foundations)
2. [Part II: Hash Functions - Theory](#part-ii-hash-functions---theory)
3. [Part III: Hash Tables - Implementation](#part-iii-hash-tables---implementation)
4. [Part IV: Advanced Hash Tables](#part-iv-advanced-hash-tables)
5. [Part V: Non-Cryptographic Hash Functions](#part-v-non-cryptographic-hash-functions)
6. [Part VI: Cryptographic Foundations](#part-vi-cryptographic-foundations)
7. [Part VII: Cryptographic Hash Construction](#part-vii-cryptographic-hash-construction)
8. [Part VIII: SHA-256 Implementation](#part-viii-sha-256-implementation)
9. [Part IX: Probabilistic Data Structures](#part-ix-probabilistic-data-structures)
10. [Part X: Distributed & Consistent Hashing](#part-x-distributed--consistent-hashing)
11. [Part XI: Blockchain Cryptographic Primitives](#part-xi-blockchain-cryptographic-primitives)
12. [Part XII: Capstone - Mini Blockchain](#part-xii-capstone---mini-blockchain)

---

## Part I: Mathematical Foundations

> You cannot understand hashing without understanding the math it's built on.

### 1.1 Functions - The Mathematical Object

**Study Topics**:

- What is a function mathematically? (mapping between sets)
- Domain, codomain, range - precise definitions
- Injective (one-to-one): different inputs → different outputs
- Surjective (onto): every output is reachable
- Bijective: both injective and surjective
- Why hash functions are surjective but NOT injective (by necessity)
- The pigeonhole principle - formal statement and proof

**Key Insight**: A hash function maps infinite domain to finite codomain. Collisions aren't a bug - they're mathematically inevitable.

**Exercises**:

- [ ] Draw diagrams showing injective, surjective, bijective functions
- [ ] Prove: if |domain| > |codomain|, function cannot be injective
- [ ] Calculate: if you have 1000 items and 100 slots, minimum collisions?

### 1.2 Modular Arithmetic

**Study Topics**:

- What is modulo operation? (remainder after division)
- Congruence relation: a ≡ b (mod n)
- Properties:
  - (a + b) mod n = ((a mod n) + (b mod n)) mod n
  - (a × b) mod n = ((a mod n) × (b mod n)) mod n
- Modular addition, subtraction, multiplication
- Why modulo is perfect for "wrapping around" to fixed range
- Modular inverse: what is a⁻¹ mod n?
- When does modular inverse exist? (GCD(a,n) = 1)

**Key Insight**: Modulo gives us a way to map any number to a bounded range while preserving arithmetic properties.

**Exercises**:

- [ ] Implement `mod_add(a, b, n)`, `mod_mul(a, b, n)`
- [ ] Implement extended Euclidean algorithm for modular inverse
- [ ] Prove: (a × b) mod n = ((a mod n) × (b mod n)) mod n

### 1.3 Prime Numbers and Their Properties

**Study Topics**:

- Fundamental theorem of arithmetic (unique prime factorization)
- Why primes minimize patterns in modular arithmetic
- Distribution of primes (prime number theorem)
- Coprime/relatively prime numbers
- Euler's totient function φ(n)
- Fermat's little theorem: a^(p-1) ≡ 1 (mod p) for prime p
- Why we use prime table sizes in hash tables
- Why we use prime multipliers in hash functions

**Key Insight**: Primes create maximum "mixing" because they share no factors with other numbers.

**Exercises**:

- [ ] Implement Sieve of Eratosthenes
- [ ] Implement `is_coprime(a, b)`
- [ ] Implement `euler_totient(n)`
- [ ] Experiment: hash distribution with prime vs non-prime table sizes

### 1.4 Probability Fundamentals

**Study Topics**:

- Basic probability: P(A), P(A and B), P(A or B)
- Independence: P(A and B) = P(A) × P(B)
- Expected value E[X]
- The birthday problem:
  - With n people, probability two share birthday
  - Derive the formula: P ≈ 1 - e^(-n²/2k) for k possible values
  - The "birthday bound": √k items gives ~50% collision chance
- Apply to hashing: with 2^128 hash, ~2^64 items for 50% collision

**Key Insight**: The birthday paradox means collisions happen much sooner than intuition suggests. A 256-bit hash isn't safe after 2^256 attempts - it's questionable after 2^128.

**Exercises**:

- [ ] Calculate: probability of collision with 23 items in 365 slots
- [ ] Calculate: how many items until 50% collision chance for 32-bit hash?
- [ ] Simulate birthday paradox in code, verify formula

### 1.5 Binary Representation and Bit Operations

**Study Topics**:

- How computers represent integers (binary)
- Unsigned vs signed integers
- Two's complement representation
- Fixed-width integers: uint8, uint32, uint64
- Overflow behavior (wrapping)
- Endianness: big-endian vs little-endian (CRITICAL for crypto)
- Bit operations: AND, OR, XOR, NOT
- Shifts: logical left shift, logical right shift, arithmetic right shift
- Rotations: left rotate, right rotate
- Why XOR is "perfect" for mixing (reversible, uniform)

**Key Insight**: Cryptographic hashes operate on bits, not numbers. Understanding bit-level operations is mandatory.

**Exercises**:

- [ ] Implement `to_binary_string(n, bits)` showing all bits
- [ ] Implement `right_rotate(value, amount, bits=32)`
- [ ] Implement `left_rotate(value, amount, bits=32)`
- [ ] Convert between big-endian and little-endian byte arrays
- [ ] Verify: `a ^ b ^ b == a` for any a, b

---

## Part II: Hash Functions - Theory

> Before implementing, understand what we're trying to achieve and why.

### 2.1 What IS a Hash Function?

**Study Topics**:

- Formal definition: h: U → {0, 1, ..., m-1}
- Universe U (all possible keys) vs actual keys
- Compression: infinite domain → finite codomain
- Determinism requirement: same input always gives same output
- The ideal: each key equally likely to hash to any slot (uniform)

**Key Questions to Answer**:

- Why do we want fixed-size output?
- What properties make a "good" hash function?
- What's the difference between a hash function and encryption?

### 2.2 Properties of Hash Functions (Non-Cryptographic)

**Study Topics**:

- Deterministic: h(x) always returns same value
- Uniform distribution: outputs spread evenly
- Efficiency: O(1) or O(k) where k is key length
- Avalanche effect (desirable): small input change → large output change

**Measuring Quality**:

- Chi-squared test for uniformity
- Bit independence
- Collision counting

**Exercises**:

- [ ] Design experiment to test hash uniformity
- [ ] Implement chi-squared test for hash distribution
- [ ] Test various hash functions for avalanche effect

### 2.3 Collision Analysis

**Study Topics**:

- Why collisions are inevitable (pigeonhole principle)
- Birthday bound: expect collision after √m items for m slots
- Load factor α = n/m
- Expected collisions formula
- Collision probability derivation

**Key Insight**: With 32-bit hash (4 billion values), expect collision after ~77,000 items. With 64-bit, after ~5 billion.

**Exercises**:

- [ ] Derive: expected number of collisions for n items, m slots
- [ ] Calculate collision probability for various n, m combinations
- [ ] Simulate and verify theoretical predictions

### 2.4 Universal Hashing

**Study Topics**:

- Problem: for any fixed hash function, adversary can find bad inputs
- Solution: randomized hash function families
- Definition: H is universal if for random h ∈ H, P[h(x) = h(y)] ≤ 1/m
- Carter-Wegman construction: h(x) = ((ax + b) mod p) mod m
- Why this provides probabilistic guarantees
- 2-universal vs k-universal families

**Key Insight**: Universal hashing gives provable average-case guarantees even against adversarial inputs.

**Exercises**:

- [ ] Implement Carter-Wegman universal hash family
- [ ] Prove it satisfies universality property
- [ ] Test against adversarial inputs that break simple hash

---

## Part III: Hash Tables - Implementation

> Now build the data structure, understanding every design decision.

### 3.1 Basic Hash Table with Chaining

**Concepts**:

- Array of buckets (linked lists)
- Insert: hash key, append to bucket
- Search: hash key, search bucket
- Delete: hash key, delete from bucket

**Implement** (`hash_table_chaining.py`):

```
class HashTableChaining:
    __init__(self, initial_size=8)
    _hash(self, key) -> int
    insert(self, key, value) -> None
    get(self, key) -> value  # raise KeyError if missing
    delete(self, key) -> None  # raise KeyError if missing
    __contains__(self, key) -> bool
    __len__(self) -> int
    keys(self) -> Iterator
    values(self) -> Iterator
    items(self) -> Iterator
```

**Complexity Analysis**:
| Operation | Average | Worst Case | Why? |
|-----------|---------|------------|------|
| insert | O(1) | O(n) | ? |
| search | O(1) | O(n) | ? |
| delete | O(1) | O(n) | ? |

Fill in the "Why?" - understand when worst case occurs.

### 3.2 Open Addressing - Linear Probing

**Concepts**:

- All items stored directly in array (no linked lists)
- Collision: probe sequence h(k), h(k)+1, h(k)+2, ...
- Primary clustering problem
- Deletion problem: tombstones

**Implement** (`hash_table_linear.py`):

- Same interface as chaining
- Add `_DELETED` sentinel for tombstones
- Track `_count` and `_deleted_count` separately

**Deep Dive**:

- Why can't we just set deleted slots to None?
- What's the probe sequence length distribution?
- When does linear probing perform poorly?

### 3.3 Open Addressing - Quadratic Probing

**Concepts**:

- Probe sequence: h(k), h(k)+1², h(k)+2², h(k)+3², ...
- Reduces primary clustering
- Secondary clustering still occurs
- May not visit all slots! (depends on table size)

**Implement** (`hash_table_quadratic.py`):

- Same interface
- Research: what table sizes guarantee all slots visited?

**Analysis**:

- When does quadratic probing fail to find empty slot?
- Prove: if m is prime and α < 0.5, always finds slot

### 3.4 Open Addressing - Double Hashing

**Concepts**:

- Two hash functions: h1(k) and h2(k)
- Probe sequence: h1(k), h1(k)+h2(k), h1(k)+2×h2(k), ...
- h2(k) must never be 0
- h2(k) must be coprime with table size

**Implement** (`hash_table_double.py`):

- Choose h2 carefully: common choice h2(k) = PRIME - (k mod PRIME)
- Analyze: why does this eliminate clustering?

### 3.5 Dynamic Resizing

**Concepts**:

- Load factor threshold (typically 0.7 for chaining, 0.5 for open addressing)
- Grow: allocate new array 2× size, rehash all items
- Shrink (optional): when α < 0.25
- Amortized analysis: why insert is still O(1) amortized

**Implement**:

- Add `_resize(self, new_size)` to all hash tables
- Add automatic resize on insert/delete

**Amortized Analysis Exercise**:

- [ ] Prove: sequence of n inserts takes O(n) total time with doubling
- [ ] Calculate: what's the worst-case single insert time?

### 3.6 HashSet and HashMap

**Implement** (`hash_set.py`):

```
class HashSet:
    add(self, item) -> None
    remove(self, item) -> None
    discard(self, item) -> None  # no error if missing
    __contains__(self, item) -> bool
    __len__(self) -> int
    __iter__(self) -> Iterator
    union(self, other) -> HashSet
    intersection(self, other) -> HashSet
    difference(self, other) -> HashSet
    symmetric_difference(self, other) -> HashSet
    issubset(self, other) -> bool
    issuperset(self, other) -> bool
```

**Implement** (`hash_map.py`):

```
class HashMap:
    put(self, key, value) -> None
    get(self, key) -> value
    get_or_default(self, key, default) -> value
    remove(self, key) -> value
    __contains__(self, key) -> bool
    __getitem__(self, key) -> value
    __setitem__(self, key, value) -> None
    __delitem__(self, key) -> None
    __len__(self) -> int
    __iter__(self) -> Iterator  # over keys
    keys(self) -> Iterator
    values(self) -> Iterator
    items(self) -> Iterator
```

---

## Part IV: Advanced Hash Tables

> Beyond the basics - specialized techniques for specific use cases.

### 4.1 Perfect Hashing

**Study Topics**:

- Problem: can we achieve O(1) worst-case (not just average)?
- Static perfect hashing: when keys are known in advance
- FKS scheme (Fredman-Komlós-Szemerédi):
  - Two-level hashing
  - First level: n buckets
  - Second level: perfect hash within each bucket
- Space: O(n) with careful construction

**Implement** (`perfect_hash.py`):

- Build perfect hash table for fixed set of keys
- Verify O(1) worst-case lookup

### 4.2 Cuckoo Hashing

**Study Topics**:

- Two hash functions, two tables
- Each key has exactly two possible locations
- Insert: if both full, "kick out" existing item (it moves to its other location)
- Cascading evictions, cycle detection
- O(1) worst-case lookup!
- Rebuilding when cycle detected

**Implement** (`cuckoo_hash.py`):

- Two arrays, two hash functions
- Insert with eviction chain (limit iterations, rebuild on cycle)
- Lookup checks both tables

**Analysis**:

- What's the expected insertion time?
- When do cycles occur?
- How does load factor affect rebuild probability?

### 4.3 Robin Hood Hashing

**Study Topics**:

- Linear probing variant
- Track "probe distance" for each item
- On collision: if new item has traveled farther, swap
- "Rob from the rich, give to the poor"
- Reduces variance in probe distances

**Implement** (`robin_hood_hash.py`):

- Store (key, value, probe_distance) tuples
- Implement swap-on-longer-probe logic

**Analysis**:

- How does this affect expected and worst-case probe length?
- Why does this improve cache performance?

### 4.4 Hopscotch Hashing

**Study Topics**:

- Each bucket has a "neighborhood" (bitmap of nearby items)
- Items can only be in their neighborhood
- Displacement to make room
- Cache-friendly, good for concurrent access

**Implement** (`hopscotch_hash.py`):

- Define neighborhood size (e.g., 32)
- Bitmap per bucket
- Displacement algorithm

---

## Part V: Non-Cryptographic Hash Functions

> Real-world hash functions used in hash tables, checksums, etc.

### 5.1 Simple Hash Functions (Understand Failures)

**Implement and analyze** (`simple_hashes.py`):

**Division method**: h(k) = k mod m

- Why m should be prime
- Bad choices for m (powers of 2, 10, etc.)

**Multiplication method**: h(k) = floor(m × (k×A mod 1))

- Knuth's suggestion: A ≈ (√5 - 1)/2
- Why this works (golden ratio properties)

**Folding**: Split key into parts, combine

- Addition folding
- XOR folding

**Analyze**:

- [ ] Test each on sequential keys (0, 1, 2, ...)
- [ ] Test on string keys
- [ ] Identify clustering patterns

### 5.2 String Hashing

**Implement** (`string_hashes.py`):

**Simple sum** (bad):

```python
def sum_hash(s): return sum(ord(c) for c in s) % m
```

- Why "cat" and "act" collide
- Why this is terrible

**Polynomial rolling hash**:

```python
def poly_hash(s, p=31, m=10**9+9):
    h = 0
    for c in s:
        h = (h * p + ord(c)) % m
    return h
```

- Why position matters now
- Choice of p and m
- Overflow handling

**Exercises**:

- [ ] Verify "cat" ≠ "act" with polynomial hash
- [ ] Implement rolling hash for substring search (Rabin-Karp)
- [ ] Analyze collision rate on dictionary words

### 5.3 Industry Standard Non-Crypto Hashes

**Study and Implement**:

**djb2** (Dan Bernstein):

```
hash = 5381
for c in string:
    hash = ((hash << 5) + hash) + c  # hash * 33 + c
```

- Why 5381? Why 33?

**FNV-1a** (Fowler-Noll-Vo):

```
hash = FNV_offset_basis
for byte in data:
    hash ^= byte
    hash *= FNV_prime
```

- XOR then multiply (vs FNV-1: multiply then XOR)
- Why this order matters for avalanche

**MurmurHash3** (Austin Appleby):

- Study the algorithm (complex but instructive)
- Understand: mixing functions, finalization
- Why it's fast (processes 4 bytes at a time)

**xxHash**:

- Even faster than Murmur
- Study the design principles

**Implement** (`industry_hashes.py`):

- [ ] djb2
- [ ] FNV-1a (32-bit and 64-bit versions)
- [ ] MurmurHash3 (32-bit version)

**Benchmark**:

- [ ] Speed comparison on various input sizes
- [ ] Distribution quality comparison
- [ ] Avalanche effect comparison

### 5.4 Hash Quality Testing

**Implement** (`hash_quality.py`):

- Chi-squared uniformity test
- Avalanche test (flip each input bit, count output bit changes)
- Collision counting on real-world data
- SMHasher-style tests (study this test suite)

---

## Part VI: Cryptographic Foundations

> The security model and threat landscape for cryptographic hashing.

### 6.1 What "Secure" Means

**Study Topics**:

- Computational vs information-theoretic security
- What is "computationally infeasible"?
- Security parameter (e.g., 128-bit security)
- Concrete vs asymptotic security

**Key Numbers**:
| Operations | Feasibility |
|------------|-------------|
| 2^40 | Easy (seconds on laptop) |
| 2^56 | Expensive but doable |
| 2^64 | Nation-state level |
| 2^80 | Currently infeasible |
| 2^128 | Will never be feasible |
| 2^256 | Astronomical |

**Context**: Bitcoin mining does ~10^20 (≈2^67) hashes per second globally.

### 6.2 Cryptographic Hash Properties - Formal Definitions

**Pre-image Resistance** (One-wayness):

- Given h, infeasible to find m such that H(m) = h
- Security: should require 2^n work for n-bit hash

**Second Pre-image Resistance**:

- Given m1, infeasible to find m2 ≠ m1 such that H(m1) = H(m2)
- Security: should require 2^n work

**Collision Resistance**:

- Infeasible to find any m1 ≠ m2 such that H(m1) = H(m2)
- Security: 2^(n/2) due to birthday bound
- This is why 256-bit hash has "128-bit security" against collisions

**Relationships**:

- Collision resistance → Second pre-image resistance
- Neither implies pre-image resistance (theoretically)
- In practice, good designs achieve all three

**Exercises**:

- [ ] Explain why collision resistance is harder than second pre-image
- [ ] Calculate: work needed to find collision in 160-bit hash (SHA-1)
- [ ] Why is 2^80 work now considered borderline?

### 6.3 The Avalanche Effect - Strict Definition

**Strict Avalanche Criterion (SAC)**:

- Flip any single input bit
- Each output bit should flip with probability exactly 0.5
- Tests true randomness of mixing

**Bit Independence Criterion (BIC)**:

- All pairs of output bits should be independent
- No correlations between bit positions

**Exercises**:

- [ ] Test your polynomial hash for SAC (it will fail)
- [ ] Understand why crypto hashes need this
- [ ] Implement SAC test

### 6.4 Attack Models and Historical Breaks

**Study These Attacks**:

**MD5 Breaks**:

- 1996: Compression function weaknesses (Dobbertin)
- 2004: Collision found in hours (Wang et al.)
- 2008: Rogue CA certificate attack (practical impact!)
- Now: Collisions in seconds on laptop

**SHA-1 Breaks**:

- 2005: Theoretical attack (Wang et al.) - 2^69 instead of 2^80
- 2017: SHAttered - first public collision (Google)
- 2020: Chosen-prefix collision (practical forgery possible)

**Lessons**:

- "Theoretical" breaks become practical
- Hash functions have shelf life
- Must understand attack progression

**Exercises**:

- [ ] Read the SHAttered paper summary
- [ ] Understand: why was MD5 collision not just academic?
- [ ] Research: what attacks exist on SHA-256? (none practical)

### 6.5 Random Oracle Model

**Study Topics**:

- Idealized hash function concept
- Properties of a random oracle
- Why real hash functions aren't random oracles
- Provable security in ROM vs standard model
- Indifferentiability

**Key Insight**: We design hash functions to be "as close as possible" to random oracles. Deviations are potential vulnerabilities.

---

## Part VII: Cryptographic Hash Construction

> How cryptographic hashes are built from smaller components.

### 7.1 Merkle-Damgård Construction

**Study Topics**:

- The dominant paradigm (MD5, SHA-1, SHA-2)
- Structure:
  - Padding function
  - Compression function f(h, m) → h'
  - Chaining: h*i = f(h*{i-1}, m_i)
  - IV (initial value)
- Why it works: if f is collision-resistant, so is full hash
- Strengthening: include length in final block

**Diagram**:

```
         m_1        m_2        m_3
          ↓          ↓          ↓
IV → [  f  ] → [  f  ] → [  f  ] → H(m)
          ↑          ↑          ↑
        h_0        h_1        h_2
```

**Implement** (`merkle_damgard.py`):

- Generic Merkle-Damgård construction
- Plug in different compression functions
- Implement padding

### 7.2 Length Extension Attack

**The Vulnerability**:

- Given H(m) and len(m), can compute H(m || padding || m') without knowing m
- Why: the hash state IS the output, and we can continue from there
- Affects: MD5, SHA-1, SHA-256 (but not SHA-3 or HMAC)

**Real-World Impact**:

- API authentication bypass
- Signature forgery
- Why HMAC exists

**Implement** (`length_extension.py`):

- Demonstrate the attack on your Merkle-Damgård hash
- Verify you can extend without knowing original message

### 7.3 Compression Function Designs

**Study These Constructions**:

**Davies-Meyer** (used in SHA-256):

```
h_i = E_{m_i}(h_{i-1}) ⊕ h_{i-1}
```

- E is a block cipher with message block as key
- XOR with input prevents easy inversion

**Matyas-Meyer-Oseas**:

```
h_i = E_{h_{i-1}}(m_i) ⊕ m_i
```

**Miyaguchi-Preneel**:

```
h_i = E_{h_{i-1}}(m_i) ⊕ m_i ⊕ h_{i-1}
```

**Key Insight**: These all use block ciphers as building blocks. SHA-256's compression function is essentially a specialized block cipher.

### 7.4 The Sponge Construction (SHA-3)

**Study Topics**:

- Alternative to Merkle-Damgård
- State divided into: rate (r) and capacity (c)
- Absorbing phase: XOR input into rate, apply permutation
- Squeezing phase: output from rate, apply permutation
- NOT vulnerable to length extension

**Diagram**:

```
Absorbing:     Squeezing:
  m_1  m_2       z_1  z_2
   ↓    ↓         ↑    ↑
  [r]  [r]       [r]  [r]
  [c]  [c]       [c]  [c]
    ↓    ↓         ↓
   [f]  [f]      [f]
```

**Why Sponge is Better**:

- Simpler security proof
- No length extension
- Variable output length natural

**Implement** (`sponge.py`):

- Generic sponge construction
- Use a simple permutation first (to understand structure)

---

## Part VIII: SHA-256 Implementation

> Build Bitcoin's hash function from scratch.

### 8.1 SHA-256 Overview

**Facts**:

- Published: 2001 (NIST)
- Output: 256 bits (32 bytes)
- Block size: 512 bits (64 bytes)
- Rounds: 64
- Operations: AND, XOR, NOT, ADD mod 2^32, ROTATE
- No known practical attacks

### 8.2 Constants

**Implement** (`sha256/constants.py`):

**Initial Hash Values (H)**: First 32 bits of fractional parts of square roots of first 8 primes:

```
H[0] = 0x6a09e667  # sqrt(2)
H[1] = 0xbb67ae85  # sqrt(3)
H[2] = 0x3c6ef372  # sqrt(5)
H[3] = 0xa54ff53a  # sqrt(7)
H[4] = 0x510e527f  # sqrt(11)
H[5] = 0x9b05688c  # sqrt(13)
H[6] = 0x1f83d9ab  # sqrt(17)
H[7] = 0x5be0cd19  # sqrt(19)
```

**Round Constants (K)**: First 32 bits of fractional parts of cube roots of first 64 primes.

**Exercise**: Generate these constants yourself:

- [ ] Implement `fractional_bits(x, bits=32)` - extract fractional part as integer
- [ ] Generate H from sqrt of primes
- [ ] Generate K from cbrt of primes
- [ ] Verify against published constants

### 8.3 Preprocessing

**Implement** (`sha256/preprocessing.py`):

**Padding**:

1. Append bit '1' to message
2. Append zeros until length ≡ 448 (mod 512)
3. Append original length as 64-bit big-endian integer

```python
def pad_message(message: bytes) -> bytes:
    """Pad message to multiple of 512 bits (64 bytes)"""
    pass

def parse_blocks(padded: bytes) -> list[bytes]:
    """Split into 512-bit (64-byte) blocks"""
    pass
```

**Test Cases**:

- Empty message → 1 block
- "abc" (24 bits) → 1 block
- 55 bytes → 1 block
- 56 bytes → 2 blocks (boundary case!)
- 64 bytes → 2 blocks

### 8.4 Message Schedule

**Implement** (`sha256/schedule.py`):

Expand 16 words to 64 words:

```
W[0..15] = message block words (big-endian)
W[i] = σ1(W[i-2]) + W[i-7] + σ0(W[i-15]) + W[i-16]  for i in 16..63
```

Where:

```
σ0(x) = ROTR(x, 7) ⊕ ROTR(x, 18) ⊕ SHR(x, 3)
σ1(x) = ROTR(x, 17) ⊕ ROTR(x, 19) ⊕ SHR(x, 10)
```

**Implement**:

```python
def sigma0(x: int) -> int:
    """Small sigma 0: ROTR7 ^ ROTR18 ^ SHR3"""
    pass

def sigma1(x: int) -> int:
    """Small sigma 1: ROTR17 ^ ROTR19 ^ SHR10"""
    pass

def create_message_schedule(block: bytes) -> list[int]:
    """Create 64-word message schedule from 64-byte block"""
    pass
```

### 8.5 Compression Function

**Implement** (`sha256/compression.py`):

**Working Variables**: a, b, c, d, e, f, g, h (each 32 bits)

**Big Sigma Functions**:

```
Σ0(x) = ROTR(x, 2) ⊕ ROTR(x, 13) ⊕ ROTR(x, 22)
Σ1(x) = ROTR(x, 6) ⊕ ROTR(x, 11) ⊕ ROTR(x, 25)
```

**Choice and Majority**:

```
Ch(x, y, z) = (x AND y) XOR (NOT x AND z)
Maj(x, y, z) = (x AND y) XOR (x AND z) XOR (y AND z)
```

**One Round**:

```
T1 = h + Σ1(e) + Ch(e, f, g) + K[i] + W[i]
T2 = Σ0(a) + Maj(a, b, c)
h = g
g = f
f = e
e = d + T1
d = c
c = b
b = a
a = T1 + T2
```

**After 64 Rounds**:
Add working variables to hash state (mod 2^32)

**Implement**:

```python
def big_sigma0(x: int) -> int: pass
def big_sigma1(x: int) -> int: pass
def ch(x: int, y: int, z: int) -> int: pass
def maj(x: int, y: int, z: int) -> int: pass

def compress(state: list[int], block: bytes, K: list[int]) -> list[int]:
    """One compression round: process 512-bit block"""
    pass
```

### 8.6 Full SHA-256

**Implement** (`sha256/sha256.py`):

```python
def sha256(message: bytes) -> bytes:
    """Compute SHA-256 hash of message"""
    # 1. Pad message
    # 2. Parse into blocks
    # 3. Initialize hash state
    # 4. For each block: compress
    # 5. Return final state as bytes
    pass

def sha256_hex(message: bytes) -> str:
    """Return hash as hex string"""
    pass
```

### 8.7 Testing and Verification

**Official Test Vectors** (NIST):

```
SHA256("") = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
SHA256("abc") = ba7816bf8f01cfea414140de5dae2223b66eafa16dfcd1fb69c7dd3c0a6a3f2b
SHA256("abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq") = 248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1
```

**Test**:

- [ ] Empty string
- [ ] "abc"
- [ ] Long message (multiple blocks)
- [ ] Compare against Python's hashlib.sha256()
- [ ] Benchmark speed

---

## Part IX: Probabilistic Data Structures

> Hash-based structures that trade accuracy for massive space savings.

### 9.1 Bloom Filters

**Concept**:

- Space-efficient probabilistic set membership
- False positives possible, false negatives impossible
- Uses k hash functions and m-bit array

**Operations**:

- Insert: set bits at h1(x), h2(x), ..., hk(x) to 1
- Query: check if ALL bits at h1(x), ..., hk(x) are 1

**Math**:

- False positive probability: (1 - e^(-kn/m))^k
- Optimal k = (m/n) × ln(2)

**Implement** (`bloom_filter.py`):

```python
class BloomFilter:
    __init__(self, expected_items: int, false_positive_rate: float)
    add(self, item) -> None
    __contains__(self, item) -> bool  # may return false positive

    # Calculate optimal m and k from parameters
```

**Exercises**:

- [ ] Derive optimal k formula
- [ ] Test false positive rate matches prediction
- [ ] Implement counting Bloom filter (supports delete)

### 9.2 Count-Min Sketch

**Concept**:

- Approximate frequency counting
- Space: O(1/ε × log(1/δ)) for ε error, δ failure probability
- Never underestimates (may overestimate)

**Implement** (`count_min_sketch.py`):

```python
class CountMinSketch:
    __init__(self, width: int, depth: int)
    add(self, item, count=1) -> None
    estimate(self, item) -> int
```

**Use Cases**:

- Network traffic monitoring
- Database query optimization
- Heavy hitters detection

### 9.3 HyperLogLog

**Concept**:

- Estimate cardinality (count distinct elements)
- Space: O(log log n) for counting n distinct elements!
- Uses: longest run of leading zeros in hash

**Key Insight**: If hashes are random, expected longest run of leading zeros indicates how many items seen.

**Implement** (`hyperloglog.py`):

```python
class HyperLogLog:
    __init__(self, precision: int = 14)  # 2^14 = 16384 registers
    add(self, item) -> None
    count(self) -> int
```

**Use Cases**:

- Counting unique visitors (Google)
- Counting unique queries
- Database cardinality estimation

---

## Part X: Distributed & Consistent Hashing

> Hashing for distributed systems - critical for blockchain P2P networks.

### 10.1 The Distributed Hashing Problem

**Problem**: You have N servers, want to distribute keys evenly.

**Naive Solution**: server = hash(key) % N
**Problem with Naive**: Adding/removing server redistributes almost all keys

### 10.2 Consistent Hashing

**Concept**:

- Hash both keys and servers to a ring (0 to 2^m - 1)
- Key goes to first server clockwise from its position
- Adding/removing server only affects adjacent keys

**Implement** (`consistent_hash.py`):

```python
class ConsistentHashRing:
    __init__(self, nodes: list[str], virtual_nodes: int = 100)
    add_node(self, node: str) -> None
    remove_node(self, node: str) -> None
    get_node(self, key: str) -> str
```

**Virtual Nodes**: Each physical node appears multiple times on ring for better distribution.

**Use Cases**:

- Distributed caches (Memcached)
- Database sharding
- P2P networks (blockchain nodes)
- CDNs

### 10.3 Rendezvous Hashing

**Alternative to Consistent Hashing**:

- For each key, compute score with each server
- Key goes to highest-scoring server
- Score = hash(key + server)

**Advantages**:

- Simpler to implement
- Better distribution with few servers
- No ring management

**Implement** (`rendezvous_hash.py`):

```python
class RendezvousHash:
    __init__(self, nodes: list[str])
    add_node(self, node: str) -> None
    remove_node(self, node: str) -> None
    get_node(self, key: str) -> str
```

---

## Part XI: Blockchain Cryptographic Primitives

> Everything you need to understand blockchain's use of hashing.

### 11.1 Hash Pointers

**Concept**:

- Pointer + hash of the thing it points to
- If data changes, hash won't match
- Can verify integrity by recomputing

**Use in Blockchain**:

- Each block points to previous block's hash
- Changing any block invalidates all subsequent blocks

**Implement** (`hash_pointer.py`):

```python
@dataclass
class HashPointer:
    data: Any
    hash: bytes

    def verify(self) -> bool:
        """Check if hash matches data"""
        pass
```

### 11.2 Hash Chains

**Concept**:

- Sequence of hash pointers
- Head → Block*n → Block*{n-1} → ... → Block_0
- Tamper-evident log

**Implement** (`hash_chain.py`):

```python
class HashChain:
    append(self, data: bytes) -> None
    verify(self) -> bool
    get_head_hash(self) -> bytes
```

### 11.3 Merkle Trees

**Concept**:

- Binary tree of hashes
- Leaves = hash of data
- Parents = hash of children concatenated
- Root = single hash representing all data

**Properties**:

- Membership proof: O(log n) hashes
- Detect tampering anywhere
- Used in Bitcoin for transactions

**Implement** (`merkle_tree.py`):

```python
class MerkleTree:
    __init__(self, data_blocks: list[bytes])
    get_root(self) -> bytes
    get_proof(self, index: int) -> list[tuple[bytes, str]]  # (hash, 'left'/'right')

    @staticmethod
    def verify_proof(leaf: bytes, proof: list, root: bytes) -> bool
```

**Exercises**:

- [ ] Build tree from list of transactions
- [ ] Generate and verify membership proofs
- [ ] Understand: how does light client use this?

### 11.4 Commitment Schemes

**Problem**: Alice wants to commit to a value without revealing it, reveal later.

**Hash-Based Commitment**:

- Commit: publish H(value || random_nonce)
- Reveal: publish value and nonce
- Anyone can verify: compute hash, compare

**Properties**:

- Hiding: can't determine value from commitment
- Binding: can't change value after commitment

**Implement** (`commitment.py`):

```python
class Commitment:
    @staticmethod
    def commit(value: bytes) -> tuple[bytes, bytes]:  # (commitment, nonce)
        pass

    @staticmethod
    def verify(value: bytes, nonce: bytes, commitment: bytes) -> bool:
        pass
```

### 11.5 Hash-Based Signatures (Lamport)

**Concept**:

- One-time signature from hash functions only
- No elliptic curves, quantum-resistant
- Key insight: reveal preimages based on message bits

**Lamport Signature**:

- Private key: 256 pairs of random 256-bit values
- Public key: hash of each private key value (512 hashes)
- Sign: for each bit of message hash, reveal one of the pair
- Verify: hash revealed values, compare to public key

**Implement** (`lamport.py`):

```python
class LamportKeyPair:
    def __init__(self):
        self.private_key = ...  # 256 pairs of 256-bit values
        self.public_key = ...   # hash of each

    def sign(self, message: bytes) -> bytes:
        pass

    def verify(self, message: bytes, signature: bytes) -> bool:
        pass
```

**Limitation**: Can only sign ONE message per key pair! (why?)

### 11.6 Proof of Work

**Concept**:

- Find nonce such that hash(data || nonce) < target
- Difficulty: number of leading zeros required
- Average work: 2^difficulty

**Bitcoin Specifics**:

- Double SHA-256: SHA256(SHA256(block_header))
- Target encoded in "bits" field
- Difficulty adjusts every 2016 blocks

**Implement** (`proof_of_work.py`):

```python
def find_nonce(data: bytes, difficulty: int) -> tuple[int, bytes]:
    """Find nonce giving hash with 'difficulty' leading zero bits"""
    pass

def verify_pow(data: bytes, nonce: int, difficulty: int) -> bool:
    pass

def calculate_difficulty(hash_bytes: bytes) -> int:
    """How many leading zero bits?"""
    pass
```

---

## Part XII: Capstone - Mini Blockchain

> Tie everything together.

### 12.1 Block Structure

**Implement** (`blockchain/block.py`):

```python
@dataclass
class BlockHeader:
    version: int
    previous_hash: bytes
    merkle_root: bytes
    timestamp: int
    difficulty: int
    nonce: int

class Block:
    header: BlockHeader
    transactions: list[bytes]

    def calculate_hash(self) -> bytes:
        """Double SHA-256 of header"""
        pass

    def calculate_merkle_root(self) -> bytes:
        pass

    def mine(self) -> None:
        """Find valid nonce"""
        pass

    def verify(self) -> bool:
        pass
```

### 12.2 Blockchain

**Implement** (`blockchain/chain.py`):

```python
class Blockchain:
    def __init__(self, difficulty: int = 4):
        self.chain: list[Block] = []
        self.difficulty = difficulty
        self._create_genesis_block()

    def add_block(self, transactions: list[bytes]) -> Block:
        pass

    def verify_chain(self) -> bool:
        """Verify entire chain integrity"""
        pass

    def get_block_by_hash(self, hash: bytes) -> Block | None:
        pass
```

### 12.3 Light Client Verification

**Implement** (`blockchain/light_client.py`):

```python
class LightClient:
    """Only stores block headers, not full blocks"""

    def __init__(self):
        self.headers: list[BlockHeader] = []

    def verify_transaction(self, tx: bytes, block_hash: bytes,
                          merkle_proof: list) -> bool:
        """Verify transaction exists in block using SPV"""
        pass
```

### 12.4 Extensions (Optional)

- Difficulty adjustment algorithm
- Simple transaction structure
- UTXO model basics
- Simple P2P network simulation

---

## Directory Structure

```
Hash/
├── HASH_MASTERY_JOURNEY.md      # This file
│
├── foundations/
│   ├── modular_arithmetic.py
│   ├── prime_utils.py
│   ├── probability.py
│   └── bit_operations.py
│
├── hash_functions/
│   ├── simple_hashes.py
│   ├── string_hashes.py
│   ├── universal_hash.py
│   └── industry_hashes.py        # djb2, FNV, MurmurHash
│
├── hash_tables/
│   ├── chaining.py
│   ├── linear_probing.py
│   ├── quadratic_probing.py
│   ├── double_hashing.py
│   ├── cuckoo.py
│   ├── robin_hood.py
│   ├── hopscotch.py
│   └── perfect_hash.py
│
├── collections/
│   ├── hash_set.py
│   └── hash_map.py
│
├── hash_quality/
│   ├── chi_squared.py
│   ├── avalanche_test.py
│   └── collision_analysis.py
│
├── crypto/
│   ├── merkle_damgard.py
│   ├── sponge.py
│   ├── length_extension.py
│   └── sha256/
│       ├── constants.py
│       ├── preprocessing.py
│       ├── schedule.py
│       ├── compression.py
│       └── sha256.py
│
├── probabilistic/
│   ├── bloom_filter.py
│   ├── count_min_sketch.py
│   └── hyperloglog.py
│
├── distributed/
│   ├── consistent_hash.py
│   └── rendezvous_hash.py
│
├── blockchain/
│   ├── hash_pointer.py
│   ├── hash_chain.py
│   ├── merkle_tree.py
│   ├── commitment.py
│   ├── lamport.py
│   ├── proof_of_work.py
│   ├── block.py
│   └── chain.py
│
└── tests/
    └── ... (tests for each module)
```

---

## Progress Tracker

### Part I: Mathematical Foundations

- [ ] 1.1 Functions - understand injective/surjective/bijective
- [ ] 1.2 Modular arithmetic - implement and prove properties
- [ ] 1.3 Prime numbers - Sieve, totient, Fermat's theorem
- [ ] 1.4 Probability - birthday paradox derivation
- [ ] 1.5 Binary representation - bit operations, endianness

### Part II: Hash Functions - Theory

- [ ] 2.1 Formal definition understood
- [ ] 2.2 Properties listed and understood
- [ ] 2.3 Collision analysis - formulas derived
- [ ] 2.4 Universal hashing implemented

### Part III: Hash Tables - Implementation

- [ ] 3.1 Chaining implemented
- [ ] 3.2 Linear probing implemented
- [ ] 3.3 Quadratic probing implemented
- [ ] 3.4 Double hashing implemented
- [ ] 3.5 Dynamic resizing implemented
- [ ] 3.6 HashSet and HashMap implemented

### Part IV: Advanced Hash Tables

- [ ] 4.1 Perfect hashing understood/implemented
- [ ] 4.2 Cuckoo hashing implemented
- [ ] 4.3 Robin Hood hashing implemented
- [ ] 4.4 Hopscotch hashing implemented

### Part V: Non-Cryptographic Hash Functions

- [ ] 5.1 Simple hash failures understood
- [ ] 5.2 String hashing - polynomial rolling hash
- [ ] 5.3 Industry hashes - djb2, FNV-1a, MurmurHash
- [ ] 5.4 Hash quality testing implemented

### Part VI: Cryptographic Foundations

- [ ] 6.1 Security model understood
- [ ] 6.2 Pre-image, second pre-image, collision resistance
- [ ] 6.3 Avalanche effect - SAC understood
- [ ] 6.4 MD5/SHA-1 breaks studied
- [ ] 6.5 Random oracle model understood

### Part VII: Cryptographic Hash Construction

- [ ] 7.1 Merkle-Damgård implemented
- [ ] 7.2 Length extension attack demonstrated
- [ ] 7.3 Compression function designs studied
- [ ] 7.4 Sponge construction implemented

### Part VIII: SHA-256 Implementation

- [ ] 8.1 Overview understood
- [ ] 8.2 Constants generated from primes
- [ ] 8.3 Preprocessing implemented
- [ ] 8.4 Message schedule implemented
- [ ] 8.5 Compression function implemented
- [ ] 8.6 Full SHA-256 working
- [ ] 8.7 All test vectors passing

### Part IX: Probabilistic Data Structures

- [ ] 9.1 Bloom filter implemented
- [ ] 9.2 Count-min sketch implemented
- [ ] 9.3 HyperLogLog implemented

### Part X: Distributed & Consistent Hashing

- [ ] 10.1 Problem understood
- [ ] 10.2 Consistent hashing implemented
- [ ] 10.3 Rendezvous hashing implemented

### Part XI: Blockchain Cryptographic Primitives

- [ ] 11.1 Hash pointers implemented
- [ ] 11.2 Hash chains implemented
- [ ] 11.3 Merkle trees implemented
- [ ] 11.4 Commitment schemes implemented
- [ ] 11.5 Lamport signatures implemented
- [ ] 11.6 Proof of work implemented

### Part XII: Capstone

- [ ] 12.1 Block structure implemented
- [ ] 12.2 Blockchain implemented
- [ ] 12.3 Light client verification working

---

## Resources

**Books**:

- "Introduction to Algorithms" (CLRS) - Chapter 11: Hash Tables
- "Cryptography Engineering" (Ferguson, Schneier) - Hash functions chapter
- "Bitcoin and Cryptocurrency Technologies" (Narayanan) - Free online

**Papers**:

- Original SHA-256 specification (FIPS 180-4)
- Merkle-Damgård revisited (Coron et al.)
- SHAttered paper (Stevens et al.)

**Online**:

- SHA-256 animation: https://sha256algorithm.com/
- Blockchain demo: https://andersbrownworth.com/blockchain/

---

## Notes

_Use this section to track insights, questions, and "aha moments" as you progress._

---
