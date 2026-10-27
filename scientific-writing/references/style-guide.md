# Style Guide

## Table Of Contents

- Global Principle
- Controlled Academic English
- Reader Value And Problem Construction
- Sentence-Level Style
- Word Choice
- Mathematical Scoping
- Introductions
- Definitions And Notation
- Theorems And Proofs
- Examples And Counterexamples
- Experiments And Software
- Chapter Transitions
- LaTeX Layout QA
- Rewrite Recipes
- Safe Subtraction
- Bad-To-Good Patterns

## Global Principle

Write so that a careful reader can audit the mathematical claim without guessing the intended scope.

The target style is plain but not flat. It is economical, explicit, and theorem-aware. It avoids inflated claims, but it does not hide the contribution. The usual rhythm is:

```text
context -> limitation/gap -> precise object -> result -> scope/consequence
```

## Controlled Academic English

Use the structural discipline of ASD-STE100 without forcing mathematical prose into aircraft-manual syntax. Keep one stable name for each object, give each sentence one main logical job, use explicit referents, and prefer direct verbs. Treat sentence-length limits as prompts to inspect scope, not automatic rewrite rules. Preserve technical vocabulary, necessary passive voice, quantifiers, modality, and theorem conditions. See `asd-ste-academic-adaptation.md` for modes and the semantic checksum.

## Reader Value And Problem Construction

For introductions, abstracts, motivation paragraphs, literature reviews, conclusions, proposals, and slides, first decide why the target mathematical reader should care. Value is not inside the topic, novelty, or the author's effort. It is created when the passage helps a specific reader understand a problem they already care about.

Use McEnerney's principle in a mathematically restrained way:

```text
reader community -> accepted theorem/practice -> precise instability -> reader consequence -> scoped contribution
```

Good mathematical instabilities include:

- an assumption whose necessity or sharpness is unclear;
- a boundary case left outside existing theorems;
- a standard implementation not covered by the available analysis;
- a gap between a proof condition and an algorithmic mechanism;
- an example showing that a plausible strengthening is false;
- a numerical practice whose purpose or interpretation is unclear;
- a software barrier that prevents reliable use or comparison.

Weak value signals include:

- "This problem is important."
- "This work is novel."
- "We fill a gap."
- "Little is known about ..."
- "We are interested in ..."
- "This chapter explores ..."

Convert them into reader-facing mathematical problems.

Weak:

```text
Little is known about whether this condition is necessary.
```

Stronger:

```text
Existing error estimates apply to exact data. They do not show how perturbations in the input affect the estimate. State why that limitation matters for the current application before presenting a new bound.
```

In a literature review, prior work should enrich the problem. Do not use the review only to prove that the author has read the literature. State what the reader community has established, where the theorem scope or mechanism remains unstable, and how the present result addresses that instability.

## Sentence-Level Style

- Prefer subject-verb-object order.
- Keep one main mathematical claim per sentence.
- Use short sentences around definitions and theorem statements.
- Use longer sentences only when they list related objects under one clear grammatical frame.
- Put the mathematical object close to its verb.
- Avoid starting several consecutive sentences with "This" unless the referent is unambiguous.
- Prefer active voice for author actions: "We prove", "We define", "We compare".
- Prefer passive voice for standard facts when the actor is irrelevant: "The model is built from interpolation conditions."

## Word Choice

### Prefer

- "show", "prove", "establish", "derive", "obtain"
- "study", "consider", "focus on"
- "under", "assuming", "provided that", "in this setting"
- "suggests", "indicates", "is consistent with" for empirical claims
- "in the sense that" when a term like "optimal" or "sharp" needs a precise meaning
- "not within the scope" when intentionally excluding a direction
- "we do not address" when a reader may reasonably expect a topic

### Avoid Or Use Sparingly

- "deep", "deeply", "profound", "fundamental" without a theorem-level justification
- "perfect", "beautiful", "elegant" in thesis prose
- "novel" unless novelty is externally meaningful and not obvious from "we propose"
- "significant" unless backed by a theorem, numerical metric, or comparison
- "dramatically", "substantially", "remarkably" unless quantified
- "unveil", "shed light on", "delve into", "explore the intricate"
- "positive/negative answer" when the question could be misunderstood
- "essential" unless you state essential for what class and under what assumptions

## Mathematical Scoping

Most overstatements come from missing scope. Add scope before the claim becomes global.

Use:

```text
under the assumptions of Theorem ...
for the specified sampling rule
for this implementation
in the convex case
when the stated parameter restriction holds
away from the boundary case
for the chosen stationarity measure
with positive probability
almost surely
```

Avoid:

```text
the condition is necessary
the algorithm does not converge
the theorem gives the full answer
this proves the assumption is essential
```

unless the statement is literally true in the stated class.

Better:

```text
For the stated model and parameter range, the theorem provides the following sufficient condition.
```

```text
The result shows that this assumption cannot be removed from this convergence theorem without changing the setting.
```

## Introductions

A strong introduction does not begin too far away from the result.

Use this sequence:

1. Define the area, object, algorithm, or reader community's accepted theorem in one sentence.
2. State the standard result or practice.
3. State the reader-valued limitation: missing boundary case, uncovered implementation, unclear sharpness, hidden mechanism, or unstable comparison.
4. State why this limitation matters for interpreting the theorem, method, or software.
5. State the paper/chapter question in one sentence.
6. State the answer with scope.
7. State the organization.

Template:

```text
[Method/class] is used to solve [problem] when [information/structure] is unavailable. Existing convergence results usually require [assumption]. These results do not explain whether [assumption/parameter condition] is close to a real boundary for [specific implementation/class]. This chapter studies this question by [construction/proof route]. We prove that, under [scope], [precise theorem-level claim].
```

For thesis chapters, avoid reintroducing the entire thesis theme every time. Give the local job of the chapter and one transition from the previous chapter.

## Definitions And Notation

- Introduce notation where it first does work.
- Give the plain-language meaning immediately after important formulas.
- Distinguish a random object from its realization when both appear.
- Avoid changing notation from the source article unless the thesis has a global symbol system.
- If a symbol is local, say so or keep it visibly local.

Template:

```text
Let \(E_k\) be the event that [plain meaning]. Thus \(E_k\) occurs exactly when [operational meaning]. The proof uses \(E_k\) to control [quantity].
```

## Theorems And Proofs

### Theorem Statements

- Put assumptions before conclusions.
- Do not hide assumptions in preceding prose if the theorem depends on them.
- Split degenerate or boundary cases before formulas with logs, divisions, inverses, or strict inequalities.
- State whether the result is qualitative, quantitative, or both.

### Proofs and mathematical derivations

Apply all nine supervisor rules in `../SKILL.md`. Read
`proofs-and-derivations.md` for their application and a worked example.
State the objective and useful reduction before technical calculation when the
reader needs that orientation. Distinguish the purpose of a step from the
condition that justifies it. Use prose to clarify either one, and use concise
identities for routine algebra. Keep needed intermediate relations, introduce
auxiliary notation at use, and explicitly connect the established result to
the target. Prefer matrix/vector notation and justify necessary entrywise work.

Do not use "obvious", "easy", or praise of the argument in place of a reason
that the audience needs. Do not narrate operations that the equations already
make clear. Neither a chain of unexplained formulas nor a sentence announcing
every algebraic operation is a useful default.

## Examples And Counterexamples

Be careful with what an example proves.

- A counterexample shows that a statement is false in a class.
- It does not show that a condition is typical, necessary in practice, or sharp on average.
- If using an example to motivate a theorem, say it motivates the theorem.
- If using an example to prove a theorem cannot be improved, state the exact improvement it rules out.

Good:

```text
This example shows that the strict inequality in Theorem ... cannot be replaced by a non-strict one under the same assumptions.
```

Risky:

```text
This example shows that the assumption is essential.
```

## Experiments And Software

For software and numerical sections, use the PDFO style:

1. State the practical barrier.
2. State what the package/tool provides.
3. List distinguishing features with concrete nouns.
4. Explain experiment purpose before results.
5. Report what the experiment demonstrates, not what it "proves", unless it is a mathematical proof.

Feature-list pattern:

```text
The package has the following features.
1. Comprehensiveness. ...
2. Solver selection. ...
3. Problem preprocessing. ...
```

Use this only when the list is genuinely scan-friendly.

## Chapter Transitions

A thesis chapter should connect to the previous and next chapter through mathematical objects, not slogans.

Good transition:

```text
The preceding proof reduces the algorithmic question to a bound on partial sums. The next section studies that bound.
```

Weak transition:

```text
This opens another black box and naturally leads to the next chapter.
```

## LaTeX Layout QA

Read `latex-layout-qa.md` when editing LaTeX. It contains the formula, caption,
proof-box, float, reference, page-break, and thesis checks with the existing log
helpers. Inspect the actual affected PDF pages; a source review alone cannot
establish readable layout. Use the full-document checks for a final manuscript
or thesis audit, rather than silently expanding every local edit into one.

## Rewrite Recipes

### Remove praise without inventing a stronger result

Setting: a paper has proved that an estimator has mean-square error at most
`C/N`, where `C>0` does not depend on the positive integer sample count `N`.
The objective is to report that established upper bound clearly.

Before:

```text
Our remarkable analysis deeply reveals the excellent accuracy of the estimator.
```

After, using only the stated setting:

```text
The estimator has mean-square error at most C/N, where C is independent of N.
```

The draft's praise is replaced by the actual proved statement. The theorem in
the setting is necessary: without it, the rewrite must not invent a rate,
optimality claim, or lower bound. In particular, an upper bound alone does not
justify replacing "at most" with "is asymptotic to".

### State A Limitation Cleanly

```text
The theorem covers strictly positive regularization parameters; the zero-parameter case remains outside its scope. (Use this formulation only if that is the actual proved scope.)
```

```text
The convergence of Powell's original implementations is not analyzed here; instead, we study the interface and numerical behavior of the package.
```

### Explain a formula when its meaning helps

Setting: `Y` is the indicator of an event `E`, and the argument uses that
`Y=0` means `E` did not occur. Say that interpretation once near the definition
when the intended reader needs it. Later uses need only recall it if the
meaning or consequence is no longer apparent. Repeating the definition after
every formula adds no justification.

## Safe Subtraction

For a low-risk thesis-shortening pass, delete empty metadiscourse, repeated roadmaps, repeated contribution statements, and clearly duplicated background before touching technical exposition. Compare assumptions, quantifiers, modality, symbols, references, proof dependencies, and experimental conditions before and after every edit. Treat theorem statements, proof routes, counterexamples, parameter conditions, empirical evidence, and open P0 issues as frozen until the user approves a mathematical change. See `asd-ste-academic-adaptation.md` for the full triage and semantic checksum.

## Bad-To-Good Patterns

| Avoid | Prefer |
| --- | --- |
| "a deep insight into" | "a bound for", "a characterization of", "a condition under which" |
| "the assumption is essential" | "the assumption cannot be removed from this theorem in this setting" |
| "negative answer" | "a positive-probability failure result" |
| "positive answer" | "a convergence result", "a sufficient condition" |
| "obviously" | "by definition", "by convexity", "because ..." |
| "we explore" | "we study", "we analyze", "we compare" |
| "it is worth noting" | often delete; otherwise state the note directly |
| "in order to" | "to" |
| "due to the fact that" | "because" |
| "is able to" | "can" |
| "utilize" | "use" |

## Final Self-Audit

After rewriting, ask:

1. Can a reader point to the theorem or definition supporting each claim?
2. Does the passage distinguish proof tools from algorithmic facts?
3. Does the first sentence of each paragraph tell the reader why the paragraph exists?
4. Did any edit change a quantifier, event, or assumption?
5. Would the passage still be true if read outside the author's intended context?
