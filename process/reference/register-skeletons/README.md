# Register skeletons — copy, don't retype

These four files are the **copyable carriers** of the register schema: the frontmatter and the
keyed table header (`<!--c:key-->`), with **zero rows**. Semantics — what each field means, its
enums, the four-sign test — live in `process/REGISTERS.md`; this folder only makes that schema
copyable, because a header retyped from prose loses its keys (the test-run lesson: what is in a
vendored template gets reproduced, what is only described does not).

At setup (`product-setup` step 4), create an instance's `registers/` by **copying each file
verbatim** into `<instance>/registers/` under the same name, then editing exactly two frontmatter
values: `<product>` → the product's name, `<date>` → today. Nothing else changes: the table headers,
their column keys and their order are the schema the linter (check D) and the console read.

Seed **no rows** — a register row is seeded only for something a source states outright and no
method will produce (see `product-setup`); everything else is method work on its pass.

The full layout of a register *file* (beyond the header) is a wave-4 subject (data unification);
these skeletons deliberately carry only what the tools already read today.
