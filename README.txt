Distraction osteogenesis manuscript calculation audit

This repository preparation contains an independent arithmetic audit of aggregate results reported in the manuscript. It does not contain the original controller firmware, Raspberry Pi application, Jetson model, raw device measurements, or evidence that the system is safe for clinical use.

Run with Python 3.10 or later: python check_calculations.py
The script uses the standard library and writes calculation_checks.csv beside itself.
Inputs are explicitly entered rounded summary values from manuscript Table 7 and reported latency, timing, and classification summaries. No trial-level measurements are reconstructed or invented. Output is an arithmetic consistency check, not an independent experimental replication.

Public manuscript citation and a research-software release must wait until the underlying original artifacts are available and the release identity is verified. No Zenodo DOI has been assigned. This local folder has not been published to GitHub.

Authors requested for the associated manuscript: Shahrokh Hatefi, Javad Alizargar, Farouk Smith.
