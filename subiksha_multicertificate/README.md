# Subiksha Makeup Academy — Multi-Certificate Verification

## Public verification
The public page is `index.html`. Each certificate uses a unique ID:

`https://YOUR-USERNAME.github.io/subiksha-certificate-verification/?id=1000`

## Add future certificates
1. Open `admin.html` on the published GitHub Pages site.
2. Enter a unique certificate number and student details.
3. Click **Add / Update Certificate**.
4. Download `certificates.json`.
5. In GitHub, replace the repository's `certificates.json` with the downloaded file and commit it.
6. Generate/use the QR shown by the manager. It points to the public verification page with that ID.

## Current record
Certificate 1000 is preloaded for Kalliyany.

## Important security note
This is a static GitHub Pages system. The manager page does not write to GitHub automatically. This avoids putting a GitHub access token/password into a public website. Anyone can view `certificates.json`, so only publish information you are comfortable making public.
