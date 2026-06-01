# HowGood
Job application submission for the Senior Python Engineer role at HowGood — signed HMAC-SHA256 POST integration script and resume.
# howgood

Application materials for the **Senior Python Engineer** role at HowGood.

## Contents
- `howgood_apply.py` — submits the application via a signed (HMAC-SHA256) POST request to the HowGood apply API.
- `Sivasanthosh_Vempali_Resume.pdf` — resume.

## Usage
```bash
pip install requests
python howgood_apply.py
```
The script signs the raw JSON body with HMAC-SHA256 and sends it with the `X-HMAC-Signature` header.

**Applicant:** Sivasanthosh Vempali · Python (5 yrs) / Django (3 yrs) · Backend & Full-Stack Engineer
