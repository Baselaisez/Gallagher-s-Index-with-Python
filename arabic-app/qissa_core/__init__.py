"""qissa_core — the typed Python interpreter of Qissa's grammar law tables.

The reader (prototype/reader.html) and this package read the SAME JSON law
tables under ``content/rules``; neither holds a rule the other lacks.  The
package layout follows the four pillars of the project brief:

* ``core_grammar``        deterministic rule engines (ṣarf now; naḥw next)
* ``ml_engine``           the small transparent models and rule induction
* ``ingestion_pipeline``  treatises → law tables, stories → calibration data
* ``memory_store``        what the system knows: lexicon, attestations
"""

__version__ = "0.1.0"
