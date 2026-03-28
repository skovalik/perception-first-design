# PFD Evaluation Anti-Patterns

These are common evaluation mistakes. If you catch yourself doing any of these, stop and re-evaluate.

## 1. Solution-First Thinking

Do NOT prescribe a fix before diagnosing the layer violation. Every fix must trace to a specific layer failure with a specific psychology mechanism. "Add a CTA" is not a valid fix unless you can explain which layer it addresses and why. Diagnosis precedes prescription — always. (See PFD Learning #1: PFD only generates non-obvious solutions when used bottom-up with constraint accumulation.)

## 2. Competitive Copying

Do NOT recommend "do what [competitor] does." PFD evaluates against perception science, not against what other sites do. A competitor's approach may be popular and still violate processing fluency. Cite psychology, not trends. The question is never "what do successful sites do?" — it is "what does perception research predict will work here?"

## 3. Decoration Without Function

Do NOT flag missing visual elements unless they serve a perception function. A site does not need parallax scrolling, animated counters, gradient backgrounds, or decorative illustrations. Flag ABSENCE only when the missing element would reduce cognitive load, increase processing fluency, or improve decision architecture. A minimal site with strong fundamentals scores higher than a decorated site with weak fundamentals.

## 4. Generic "Best Practice" Advice

Do NOT cite "best practices" without a psychology mechanism. "Most sites have X" is not evidence. "X reduces cognitive load because Cowan (2010) found working memory holds 3-5 chunks" is evidence. Every recommendation must connect to a perceptual mechanism from the loaded reference material. If you cannot cite a specific study, say "practitioner observation" — do not dress up convention as science.

## 5. Severity Inflation

Do NOT mark everything as "major" or "critical." Use the full severity range. A 2px border-radius inconsistency between two button variants is minor. A missing responsive viewport meta tag is critical. Severity must match perception impact — how much does this violation degrade the user's ability to process, trust, and act on the page? Reserve "critical" for violations that block an entire layer.

## 6. Design System Projection

Do NOT assume a design system that is not there. If detection confidence is below 70%, state "no confident framework detection" and evaluate against general perception principles, not framework-specific rules. A custom-CSS site evaluated against Tailwind conventions will produce false positives. Match the evaluation to the actual implementation, not the implementation you wish were there.
