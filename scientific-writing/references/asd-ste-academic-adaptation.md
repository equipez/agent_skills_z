# ASD-STE100 Adaptation For Mathematical Writing

## Purpose

This note adapts selected ASD-STE100 principles to mathematical theses and papers. It is a clarity and error-control method, not a claim of formal ASD-STE100 compliance.

ASD-STE100 was developed for technical documentation read by an international audience. Its useful transferable ideas are structural: keep terms stable, make sentence structure explicit, put one action in each procedural sentence, and remove avoidable ambiguity. Issue 9 contains 53 writing rules in nine sections and a controlled dictionary. The official dictionary is not reproduced here.

Source overview: https://www.asd-ste100.org/about.html . This reference
adapts clarity principles to mathematical prose and does not reproduce the
standard's controlled dictionary or claim formal compliance.

## Mode Selection

### Strict Procedural Mode

Use for:

- algorithmic instructions;
- experimental procedures;
- build and release checklists;
- tool descriptions and error messages;
- instructions passed between agents.

In this mode, aim for at most 20 words per instruction. Put one action in each sentence. Use numbered steps for a sequence. Name the actor when responsibility matters.

### STE-Inspired Academic Mode

Use for:

- thesis and paper prose;
- theorem motivation and interpretation;
- literature reviews;
- proof prose;
- chapter introductions and summaries.

Do not enforce the ASD-STE100 dictionary or a hard sentence-length cap. A theorem-aware sentence may need several clauses to keep a condition and its conclusion together. Split it only when the logical scope remains explicit.

## Rules That Transfer Well

### One Concept, One Name

Create a local term ledger for important objects. For example, do not alternate among `polling set`, `direction set`, and `sampled directions` unless the terms denote different objects. If they differ, define the difference.

Do not rotate among `condition`, `assumption`, `requirement`, and `criterion` only for variety. Select the term that matches the mathematical role.

### One Main Logical Job Per Sentence

A sentence should primarily do one of these jobs:

- state an assumption;
- define an object;
- state a result;
- give a reason;
- state a consequence;
- delimit scope;
- connect two sections.

A sentence can contain subordinate mathematical conditions, but it should not also introduce a new motivation, a new result, and a qualification about future work.

### Explicit Referents

Replace ambiguous starts such as `This shows`, `It follows`, or `These results` when more than one antecedent is possible.

Prefer:

```text
The probability bound shows that ...
Combining Lemmas 3.1 and 3.2 gives ...
The two convergence theorems do not cover ...
```

### Direct Verbs

Prefer:

- `analyze` to `perform an analysis of`;
- `compare` to `make a comparison of`;
- `prove` to `provide a proof of`;
- `use` to `make use of`;
- `requires` to `is dependent on` when the dependency is mathematical.

### Stable Claim Strength

Never remove or strengthen:

- `may`, `can`, `need not`, or `is sufficient`;
- `with positive probability`, `almost surely`, or `in expectation`;
- `for all`, `there exists`, `for sufficiently large`, or `along a subsequence`;
- `under Assumption ...`, `in the convex case`, or another scope marker.

These phrases are part of the claim.

### Active And Passive Voice

Use active voice for author actions:

```text
We define the event ...
We prove that ...
Section 4 compares ...
```

Keep passive voice when the actor is irrelevant or when the mathematical object must remain the topic:

```text
The model is constructed from interpolation conditions.
The probability is conditioned on the natural filtration.
```

The goal is explicit structure, not a passive-voice count of zero.

## Rules That Do Not Transfer Literally

- Do not replace the mathematical vocabulary with the ASD-STE100 base dictionary.
- Do not split every descriptive sentence at 25 words. First inspect whether the sentence has multiple logical jobs or ambiguous scope.
- Do not ban all semicolons mechanically. Remove a semicolon when it hides two claims; retain it only when it improves a mathematically parallel construction and the house style permits it.
- Do not ban perfect tenses when chronology or present relevance matters.
- Do not force active voice when it obscures the mathematical object.
- Do not simplify notation, assumptions, or theorem language only to meet a style rule.

## Safe Compression Procedure

### 1. Freeze Meaning

Before editing, record:

- the paragraph's role;
- its theorem-level claim, if any;
- all assumptions and quantifiers;
- all cited results and cross-references;
- all terms whose names must remain stable.

### 2. Remove Low-Risk Material

Remove empty frames such as:

- `It is important to note that`;
- `It is worth mentioning that`;
- `In order to`;
- repeated descriptions of the thesis organization;
- repeated claims that a result is important, interesting, elegant, or useful;
- a second explanation that adds no new condition, mechanism, or consequence.

### 3. Consolidate Repetition

Keep the best occurrence of a definition, motivation, or conclusion. At later occurrences, use a short cross-reference only when it preserves local readability.

Do not merge two paragraphs merely because they share vocabulary. They may serve different logical roles.

### 4. Recheck The Semantic Checksum

After editing, compare:

| Dimension | Must remain unchanged unless explicitly approved |
| --- | --- |
| Scope | assumptions, parameter ranges, boundary cases |
| Logic | implication direction, necessity versus sufficiency |
| Probability | conditioning, filtration, event, almost sure versus positive probability |
| Notation | symbol meaning, index range, deterministic versus random object |
| Evidence | citation, theorem reference, experiment setting, exclusion |
| Structure | required transition and later dependency |

If a shorter version fails this check, restore the original meaning even if the sentence becomes longer.

### 5. Compile And Inspect

For LaTeX, compile after the edit. Check references, citations, labels, overfull boxes, formula breaks, captions, and page breaks. A text reduction can still introduce a bad float placement or detach a displayed formula from its explanation.

## Repository-Wide Subtraction Triage

Classify each candidate before editing:

- `S0`: empty metadiscourse, duplicate roadmap, promotional adjective. Delete directly after local review.
- `S1`: repeated background, repeated conclusion, redundant example, verbose transition. Edit after checking cross-references and later dependencies.
- `S2`: theorem interpretation, proof explanation, algorithm specification, experiment description. Shorten only with a semantic checksum and source comparison.
- `S3`: theorem statement, proof route, counterexample, parameter condition, empirical evidence, front matter required for submission, or an open P0. Do not change without explicit discussion.

For a low-risk shortening pass, edit only `S0` and clear `S1` cases.

## Acceptance Criteria

A shortening pass is acceptable only if:

- the word count decreases for the intended scope;
- every edited paragraph retains its mathematical role;
- no assumption, quantifier, qualifier, citation, or dependency disappears unintentionally;
- terminology is more stable, not merely shorter;
- the thesis compiles without new undefined references or citations;
- the edited PDF has no new layout defect;
- open P0 items remain visible and are not disguised by smoother prose.
