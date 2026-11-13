"""The learning layer: small, transparent learners whose output is rules.

Decision recorded in research/ARCHITECTURE.md: nothing learned here runs as a
black box in the app.  A learner proposes rules, a gate promotes some, and
what is promoted is written as data a person can read (``induction``).  The
reader's own models (the iʿrāb perceptron, the taggers, the rule miner) are
fitted by ``tools/`` and stay on the device.
"""
