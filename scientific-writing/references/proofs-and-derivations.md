# Proofs and mathematical derivations

The nine supervisor rules in `../SKILL.md` are the primary requirements. This
reference explains how to apply them; it does not replace or weaken them.

## Purpose, justification, and detail

Purpose answers "What will this calculation establish, and how will that help?"
Justification answers "Why is this equality, inequality, or implication valid?"
Give a short orientation when the purpose is not already apparent. Put the
relevant hypothesis, identity, or cited result at the step that needs it. Do
not add a purpose sentence before every line of an already clear chain.

For a substantial proof, identify the target and any useful reduction, explain
the mechanism, and then present the required relations. Mention how an
assumption enables the mechanism when this helps the reader. Introduce local
symbols with the construction they abbreviate. Show enough of the calculation
to expose the real dependency, and finish by connecting it to the target.
The number of stages depends on the proof.

Routine arithmetic can be expressed by a compact identity. Keep a missing
measure-theoretic condition, interchange-of-limit argument, singular case,
division by a possibly zero quantity, or probabilistic qualification visible;
these are not routine algebra to be suppressed for brevity. When using a
known inequality, identify its operands and verify its assumptions.

Label targets and intermediate results that will be referenced. Numbering every
line is unnecessary. On a later reference, identify what the result does, for
example "the displacement bound (3.8)", so the reader can follow without
repeatedly turning back.

## Matrix/vector notation

Use vector identities, norms, inner products, matrix products, factorizations,
and block notation when they express the argument. Do not introduce component
indices merely to verify a standard vector identity. Check dimensions, norm
conventions, symmetry, and transpose versus conjugate transpose as needed.

Component notation is justified when the claim actually concerns entries,
coordinate selection, sparsity, signs, or a componentwise estimate that cannot
be expressed as clearly at the matrix/vector level. Explain that local role
and return to the vector formulation when possible. This implements the
supervisor's "unless truly necessary" qualification. Higham's Gershgorin
example (§7.5, printed pp. 120–122) is an instance where a selected coordinate
is essential; it is not a reason to expand unrelated vector arguments.

## Original worked example

The following is a new illustration for this skill, not an excerpt from the
referenced sources. Let `A` be a real symmetric positive-definite matrix, let
`b` be a real vector of compatible dimension, and let `x_* = A^{-1}b`.
For `f(x) = (1/2)x^T A x - b^T x`, the target is

```latex
\begin{equation}\label{eq:quadratic-gap-target}
  f(x)-f(x_*) \geq
  \tfrac12\lambda_{\min}(A)\|x-x_*\|_2^2.
\end{equation}
```

An unhelpful draft might expand all entries, repeatedly announce that terms
are being multiplied or collected, and end after an algebraic expansion
without connecting the calculation to this inequality.

A useful version for a numerical-analysis reader is:

> We express the objective gap in terms of the displacement from the minimizer;
> the smallest eigenvalue will then give the required lower bound. Set
> `e=x-x_*`. Since `Ax_*=b` and `A` is symmetric,

```latex
\begin{align*}
  f(x)-f(x_*)
    &= e^T(Ax_*-b)+\tfrac12 e^TAe \\
    &= \tfrac12 e^TAe \\
    &\geq \tfrac12\lambda_{\min}(A)\|e\|_2^2.
\end{align*}
```

> Substituting `e=x-x_*` proves the target inequality.

The first sentence supplies purpose, `e` is introduced at use, symmetry and
stationarity justify the expansion/cancellation, and the Rayleigh bound gives
the final inequality. No entrywise expansion or computation of all eigenvalues
is needed. If the audience needs the Rayleigh bound explained, add that
explanation at the last step. If the target is visible immediately above and
will not be referenced elsewhere, an unnumbered display is sufficient.

## Public exemplar

For a software/method exposition example, inspect Ragonneau and Zhang's PDFO
paper, §3.1.2. It states the interpolation conditions and their degrees of
freedom, then uses the initial evaluation cost to motivate underdetermined
quadratic interpolation. Learn the organization; check every mathematical
claim against the current manuscript rather than copying another paper's
conclusions. Bibliographic details are in `source-corpus.md`.
