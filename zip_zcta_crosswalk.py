"""
zip_zcta_crosswalk.py
=====================
Crosswalk for 37 institutional/campus USPS ZIP codes that do not exist in the
US Census ZCTA shapefile (because they are unique-organisation or PO-Box ZIPs).

Each entry maps an institutional ZIP to the nearest residential ZCTA ZIP,
determined by Haversine distance between the known hospital latitude/longitude
and every ZCTA centroid in the project's ZCTA base file.

Maximum geographic offset: 2.10 miles (UNC Chapel Hill, 27599 → 27510).
All offsets are negligible relative to the 30-mile and 60-mile access radii
used in the access analysis.

Methodology reference:
  "Clinical trial sites using institutional or PO Box USPS ZIP codes that do
   not map to standard Census ZIP Code Tabulation Areas (ZCTAs) were
   geographically crosswalked to their surrounding residential ZCTA to preserve
   trial location integrity for spatial analysis."

Generated: 2026-05-22  |  Project: CAR-T Geographic Access (JAMA Manuscript)
"""

# Keys   = institutional/campus ZIP (from ClinicalTrials.gov)
# Values = nearest residential ZCTA ZIP (for lat/lon lookup only)
ZIP_TO_ZCTA_CROSSWALK = {
    '02214': '02203',   # Boston, MA          | Local Institution
    '03756': '03766',   # Lebanon, NH         | Dartmouth-Hitchcock Medical Center
    '06520': '06511',   # New Haven, CT       | Yale School of Medicine
    '08903': '08901',   # New Brunswick, NJ   | Rutgers Cancer Institute of NJ
    '14263': '14202',   # Buffalo, NY         | Roswell Park Cancer Institute
    '14642': '14604',   # Rochester, NY       | University of Rochester / Research Site
    '18711': '18701',   # Wilkes-Barre, PA    | Geisinger Wyoming Valley
    '20892': '20814',   # Bethesda, MD        | NIH Clinical Center
    '21287': '21231',   # Baltimore, MD       | Johns Hopkins Sidney Kimmel
    '22908': '22904',   # Charlottesville, VA | UVA Health
    '23298': '23219',   # Richmond, VA        | VCU Massey Cancer Center
    '27157': '27110',   # Winston-Salem, NC   | Atrium Health Wake Forest Baptist
    '27599': '27510',   # Chapel Hill, NC     | UNC Lineberger
    '27708': '27701',   # Durham, NC          | Duke University
    '27710': '27701',   # Durham, NC          | Duke University Medical Center
    '29425': '29424',   # Charleston, SC      | MUSC / Research Site
    '32610': '32612',   # Gainesville, FL     | UF Health Cancer Institute
    '35294': '35233',   # Birmingham, AL      | University of Alabama at Birmingham
    '37232': '37219',   # Nashville, TN       | Vanderbilt / Research Site
    '40506': '40507',   # Lexington, KY       | University of Kentucky
    '40536': '40507',   # Lexington, KY       | University of Kentucky Medical
    '44195': '44106',   # Cleveland, OH       | Cleveland Clinic Taussig Cancer Center
    '45221': '45219',   # Cincinnati, OH      | University of Cincinnati
    '45267': '45219',   # Cincinnati, OH      | University of Cincinnati Medical
    '58122': '58105',   # Fargo, ND           | Sanford Broadway Medical Center
    '60208': '60201',   # Evanston, IL        | Northwestern University
    '65212': '65215',   # Columbia, MO        | University of Missouri - Ellis Fischel
    '66068': '60068',   # Park Ridge, IL      | Advocate Aurora Health
    '66160': '64106',   # Kansas City, KS     | University of Kansas Medical Center
    '68198': '68132',   # Omaha, NE           | University of Nebraska Medical Center
    '84142': '84111',   # Salt Lake City, UT  | Intermountain Health LDS Hospital
    '84143': '84111',   # Salt Lake City, UT  | Intermountain Healthcare
    '91817': '95814',   # Sacramento, CA      | UC Davis Comprehensive Cancer Center
    '92073': '92037',   # La Jolla, CA        | UC San Diego Moores Cancer Center
    '92093': '92037',   # La Jolla, CA        | Research Site (UCSD campus)
    '94035': '94301',   # Palo Alto, CA       | Stanford Cancer Institute
    '94143': '94117',   # San Francisco, CA   | University of California San Francisco
}
