import alpaca_trade_api as tradeapi
import threading
import time
import datetime

API_KEY = "PK4Z0YF9DJ1NYYZTAPVP"
API_SECRET = "BwXQtmt91OIlwiVoCnNM9OzjWIKADpuPaBGskmA2"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"


class LongShort:
  def __init__(self):
    self.alpaca = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, 'v2')

    stockUniverse = ['A',	'AA',	'AAN',	'AAP',	'AAT',	'AB',	'ABB',	'ABBV',	'ABC',	'ABEV',	'ABG',	'ABM',	'ABR',	'ABR-A',	'ABR-B',	'ABR-C',	'ABT',	'AC',	'ACA',	'ACB',	'ACC',	'ACCO',	'ACE.W',	'ACEL',	'ACH',	'ACM',	'ACN',	'ACP',	'ACRE',	'ACV',	'ADC',	'ADM',	'ADNT',	'ADS',	'ADSW',	'ADT',	'ADX',	'AEB',	'AEE',	'AEFC',	'AEG',	'AEL',	'AEL-A',	'AEM',	'AEO',	'AEP',	'AEP-B',	'AER',	'AES',	'AFB',	'AFC',	'AFG',	'AFGB',	'AFGC',	'AFGH',	'AFI',	'AFL',	'AFT',	'AG',	'AGCO',	'AGD',	'AGI',	'AGM',	'AGM-A',	'AGM-C',	'AGM-D',	'AGM.A',	'AGN',	'AGO',	'AGO-B',	'AGO-E',	'AGO-F',	'AGR',	'AGRO',	'AGS',	'AGX',	'AHC',	'AHH',	'AHH-A',	'AHL-C',	'AHL-D',	'AHL-E',	'AHT',	'AHT-D',	'AHT-F',	'AHT-G',	'AHT-H',	'AHT-I',	'AI',	'AI-B',	'AI-C',	'AIC',	'AIF',	'AIG',	'AIG-A',	'AIG.W',	'AIN',	'AIO',	'AIR',	'AIT',	'AIV',	'AIW',	'AIZ',	'AIZP',	'AJG',	'AJRD',	'AJX',	'AJXA',	'AKO.A',	'AKO.B',	'AKR',	'AKS',	'AL',	'AL-A',	'ALB',	'ALC',	'ALE',	'ALEX',	'ALG',	'ALI-A',	'ALI-B',	'ALI-E',	'ALK',	'ALL',	'ALL-B',	'ALL-G',	'ALL-H',	'ALL-I',	'ALL-Y',	'ALLE',	'ALLY',	'ALP-Q',	'ALSN',	'ALT.W',	'ALTG',	'ALU.U',	'ALU.W',	'ALUS',	'ALV',	'ALX',	'AM',	'AMB.W',	'AMBC',	'AMC',	'AMCR',	'AME',	'AMG',	'AMH',	'AMH-D',	'AMH-E',	'AMH-F',	'AMH-G',	'AMH-H',	'AMK',	'AMN',	'AMOV',	'AMP',	'AMPY',	'AMRC',	'AMRX',	'AMT',	'AMX',	'AN',	'ANET',	'ANF',	'ANH',	'ANH-A',	'ANH-B',	'ANH-C',	'ANTM',	'AOD',	'AON',	'AOS',	'AP',	'APA',	'APAM',	'APD',	'APH',	'APHA',	'APLE',	'APO',	'APO-A',	'APO-B',	'APRN',	'APTS',	'APTV',	'APY',	'AQN',	'AQNA',	'AQNB',	'AQUA',	'AR',	'ARA',	'ARC',	'ARCH',	'ARCO',	'ARD',	'ARDC',	'ARE',	'ARE-A',	'ARES',	'ARGD',	'ARGO',	'ARI',	'ARL',	'ARLO',	'ARMK',	'ARNC',	'AROC',	'ARR',	'ARR-C',	'ARW',	'ASA',	'ASB',	'ASB-C',	'ASB-D',	'ASB-E',	'ASC',	'ASG',	'ASGN',	'ASH',	'ASIX',	'ASPN',	'ASR',	'ASX',	'AT',	'ATC-D',	'ATC-E',	'ATC-G',	'ATC-H',	'ATC-I',	'ATCO',	'ATEN',	'ATGE',	'ATH',	'ATH-A',	'ATH-B',	'ATHM',	'ATI',	'ATKR',	'ATO',	'ATR',	'ATTO',	'ATUS',	'ATV',	'AU',	'AUY',	'AVA',	'AVAL',	'AVB',	'AVD',	'AVH',	'AVK',	'AVLR',	'AVNS',	'AVT-A',	'AVTR',	'AVX',	'AVY',	'AVYA',	'AWF',	'AWI',	'AWK',	'AWP',	'AWR',	'AX',	'AXE',	'AXL',	'AXO',	'AXP',	'AXR',	'AXS',	'AXS-E',	'AXTA',	'AYI',	'AYR',	'AYX',	'AZN',	'AZO',	'AZRE',	'AZUL',	'AZZ',	'B',	'BA',	'BABA',	'BAC',	'BAC-A',	'BAC-B',	'BAC-C',	'BAC-E',	'BAC-K',	'BAC-L',	'BAC-M',	'BAC-N',	'BAF',	'BAH',	'BAK',	'BAM',	'BAN-D',	'BAN-E',	'BANC',	'BAP',	'BAX',	'BB',	'BBAR',	'BBD',	'BBDC',	'BBDO',	'BBF',	'BBK',	'BBL',	'BBN',	'BBU',	'BBVA',	'BBW',	'BBX',	'BBY',	'BC',	'BC-A',	'BC-B',	'BC-C',	'BCC',	'BCE',	'BCEI',	'BCH',	'BCO',	'BCRH',	'BCS',	'BCSF',	'BCX',	'BDC',	'BDJ',	'BDN',	'BDX',	'BDXA',	'BE',	'BEDU',	'BEN',	'BEP',	'BEP-A',	'BERY',	'BEST',	'BF.A',	'BF.B',	'BFAM',	'BFK',	'BFO',	'BFS',	'BFS-D',	'BFS-E',	'BFY',	'BFZ',	'BG',	'BGB',	'BGG',	'BGH',	'BGIO',	'BGR',	'BGS',	'BGSF',	'BGT',	'BGX',	'BGY',	'BH',	'BH.A',	'BHC',	'BHE',	'BHK',	'BHLB',	'BHP',	'BHR',	'BHR-B',	'BHR-D',	'BHV',	'BHVN',	'BIF',	'BIG',	'BILL',	'BIO',	'BIO.B',	'BIP',	'BIP.P',	'BIPC',	'BIT',	'BITA',	'BJ',	'BK',	'BK-C',	'BKD',	'BKE',	'BKH',	'BKI',	'BKK',	'BKN',	'BKR',	'BKT',	'BKU',	'BLD',	'BLE',	'BLK',	'BLL',	'BLW',	'BLX',	'BMA',	'BME',	'BMEZ',	'BMI',	'BML-G',	'BML-H',	'BML-J',	'BML-L',	'BMO',	'BMY',	'BMY.P',	'BNED',	'BNS',	'BNY',	'BOE',	'BOH',	'BOOT',	'BORR',	'BOX',	'BP',	'BPMP',	'BPT',	'BQH',	'BR',	'BRBR',	'BRC',	'BRFS',	'BRK.A',	'BRK.B',	'BRMK',	'BRO',	'BRT',	'BRX',	'BSA',	'BSAC',	'BSBR',	'BSD',	'BSE',	'BSIG',	'BSL',	'BSM',	'BSMX',	'BST',	'BSTZ',	'BSX',	'BTA',	'BTE',	'BTI',	'BTO',	'BTT',	'BTU',	'BTZ',	'BUD',	'BUI',	'BURL',	'BV',	'BVN',	'BW',	'BWA',	'BWG',	'BWXT',	'BX',	'BXC',	'BXG',	'BXMT',	'BXMX',	'BXP',	'BXP-B',	'BXS',	'BXS-A',	'BY',	'BYD',	'BYM',	'BZH',	'BZM',	'C',	'C-J',	'C-K',	'C-N',	'C-S',	'CAAP',	'CABO',	'CACI',	'CADE',	'CAE',	'CAF',	'CAG',	'CAH',	'CAI',	'CAI-A',	'CAI-B',	'CAJ',	'CAL',	'CALX',	'CANG',	'CAPL',	'CAR.P',	'CARS',	'CAT',	'CATO',	'CB',	'CBB',	'CBB-B',	'CBD',	'CBH',	'CBL',	'CBL-D',	'CBL-E',	'CBRE',	'CBT',	'CBU',	'CBZ',	'CC',	'CCA.U',	'CCC',	'CCEP',	'CCH',	'CCH.U',	'CCH.W',	'CCI',	'CCI-A',	'CCJ',	'CCK',	'CCL',	'CCM',	'CCO',	'CCR',	'CCS',	'CCU',	'CCX',	'CCX.U',	'CCX.W',	'CCZ',	'CDAY',	'CDE',	'CDR',	'CDR-B',	'CDR-C',	'CE',	'CEA',	'CEE',	'CEIX',	'CEL',	'CEL.P',	'CELP',	'CEM',	'CEN',	'CEO',	'CEPU',	'CEQ.P',	'CEQP',	'CF',	'CFG',	'CFG-D',	'CFG-E',	'CFR',	'CFR-A',	'CFX',	'CFXA',	'CGA',	'CGC',	'CHA',	'CHAP',	'CHCT',	'CHD',	'CHE',	'CHGG',	'CHH',	'CHK',	'CHK-D',	'CHL',	'CHM-A',	'CHM-B',	'CHMI',	'CHN',	'CHRA',	'CHS',	'CHT',	'CHU',	'CHWY',	'CI',	'CIA',	'CIB',	'CIEN',	'CIF',	'CIG',	'CIG.C',	'CII',	'CIM',	'CIM-A',	'CIM-B',	'CIM-C',	'CIM-D',	'CINR',	'CIO',	'CIO-A',	'CIR',	'CIT',	'CIT-B',	'CKH',	'CL',	'CLB',	'CLDR',	'CLDT',	'CLF',	'CLGX',	'CLH',	'CLI',	'CLN-G',	'CLN-H',	'CLN-I',	'CLN-J',	'CLNC',	'CLNY',	'CLPR',	'CLR',	'CLS',	'CLW',	'CLX',	'CM',	'CMA',	'CMC',	'CMCM',	'CMD',	'CMG',	'CMI',	'CMO',	'CMO-E',	'CMP',	'CMR-B',	'CMR-C',	'CMR-D',	'CMR-E',	'CMRE',	'CMS',	'CMS-B',	'CMSA',	'CMSC',	'CMSD',	'CMU',	'CNA',	'CNC',	'CNF',	'CNHI',	'CNI',	'CNK',	'CNMD',	'CNNE',	'CNO',	'CNP',	'CNP-B',	'CNQ',	'CNR',	'CNS',	'CNX',	'CNXM',	'CO',	'COD-A',	'COD-B',	'COD-C',	'CODI',	'COE',	'COF',	'COF-F',	'COF-G',	'COF-H',	'COF-I',	'COF-J',	'COG',	'COLD',	'COO',	'COP',	'COR',	'COR-Z',	'CORR',	'COTY',	'CP',	'CPA',	'CPAC',	'CPB',	'CPE',	'CPF',	'CPG',	'CPK',	'CPLG',	'CPRI',	'CPS',	'CPT',	'CR',	'CRC',	'CRD.A',	'CRD.B',	'CRH',	'CRI',	'CRK',	'CRL',	'CRM',	'CRS',	'CRT',	'CRY',	'CS',	'CSL',	'CSLT',	'CSPR',	'CSTM',	'CSU',	'CSV',	'CTA-A',	'CTA-B',	'CTAA',	'CTB',	'CTBB',	'CTDD',	'CTK',	'CTL',	'CTLT',	'CTR',	'CTRA',	'CTS',	'CTST',	'CTT',	'CTV',	'CTVA',	'CTY',	'CTZ',	'CUB',	'CUB-C',	'CUB-D',	'CUB-E',	'CUB-F',	'CUBB',	'CUBE',	'CUBI',	'CUK',	'CULP',	'CURO',	'CUZ',	'CVA',	'CVE',	'CVEO',	'CVI',	'CVIA',	'CVNA',	'CVS',	'CVX',	'CW',	'CWE.A',	'CWEN',	'CWH',	'CWK',	'CWT',	'CX',	'CXE',	'CXH',	'CXO',	'CXP',	'CXW',	'CYD',	'CYH',	'CZZ',	'D',	'DAC',	'DAL',	'DAN',	'DAO',	'DAR',	'DAVA',	'DB',	'DBD',	'DBI',	'DBL',	'DCF',	'DCI',	'DCO',	'DCP',	'DCP-B',	'DCP-C',	'DCUE',	'DD',	'DDD',	'DDF',	'DDS',	'DDT',	'DE',	'DEA',	'DECK',	'DEI',	'DELL',	'DEO',	'DESP',	'DEX',	'DFIN',	'DFN.U',	'DFNS',	'DFP',	'DFS',	'DG',	'DGX',	'DHF',	'DHI',	'DHR',	'DHR-A',	'DHT',	'DHX',	'DIAX',	'DIN',	'DIS',	'DK',	'DKL',	'DKS',	'DL',	'DLB',	'DLN-A',	'DLN-B',	'DLNG',	'DLPH',	'DLR',	'DLR-C',	'DLR-G',	'DLR-I',	'DLR-J',	'DLR-K',	'DLR-L',	'DLX',	'DLY',	'DMB',	'DMO',	'DMY.U',	'DNI',	'DNK',	'DNOW',	'DNP',	'DNR',	'DO',	'DOC',	'DOOR',	'DOV',	'DOW',	'DPG',	'DPZ',	'DQ',	'DRD',	'DRE',	'DRH',	'DRI',	'DRQ',	'DRUA',	'DS',	'DS-B',	'DS-C',	'DS-D',	'DSE',	'DSL',	'DSM',	'DSSI',	'DSU',	'DSX',	'DSX-B',	'DT',	'DTE',	'DTF',	'DTJ',	'DTL.P',	'DTP',	'DTQ',	'DTW',	'DTY',	'DUC',	'DUK',	'DUK-A',	'DUKB',	'DUKH',	'DVA',	'DVD',	'DVN',	'DX',	'DX-A',	'DX-B',	'DX-C',	'DXB',	'DXC',	'DY',	'E',	'EAB',	'EAE',	'EAF',	'EAI',	'EARN',	'EAT',	'EB',	'EBF',	'EBR',	'EBR.B',	'EBS',	'EC',	'ECC',	'ECCB',	'ECCX',	'ECCY',	'ECL',	'ECOM',	'ECT',	'ED',	'EDD',	'EDF',	'EDI',	'EDN',	'EDU',	'EE',	'EEA',	'EEX',	'EFC',	'EFC-A',	'EFF',	'EFL',	'EFR',	'EFT',	'EFX',	'EGF',	'EGHT',	'EGIF',	'EGO',	'EGP',	'EGY',	'EHC',	'EHI',	'EHT',	'EIC',	'EIG',	'EIX',	'EL',	'ELAN',	'ELAT',	'ELC',	'ELF',	'ELJ',	'ELP',	'ELS',	'ELU',	'ELVT',	'ELY',	'EMD',	'EME',	'EMF',	'EMN',	'EMO',	'EMP',	'EMR',	'ENB',	'ENBA',	'ENBL',	'ENIA',	'ENIC',	'ENJ',	'ENLC',	'ENO',	'ENR',	'ENR-A',	'ENS',	'ENV',	'ENVA',	'ENZ',	'EOD',	'EOG',	'EOI',	'EOS',	'EOT',	'EP-C',	'EPAC',	'EPAM',	'EPC',	'EPD',	'EPR',	'EPR-C',	'EPR-E',	'EPR-G',	'EPRT',	'EQC',	'EQC-D',	'EQH',	'EQH-A',	'EQM',	'EQNR',	'EQR',	'EQS',	'EQT',	'ERA',	'ERF',	'ERJ',	'EROS',	'ES',	'ESE',	'ESI',	'ESNT',	'ESRT',	'ESS',	'ESTC',	'ESTE',	'ET',	'ETB',	'ETG',	'ETH',	'ETI.P',	'ETJ',	'ETM',	'ETN',	'ETO',	'ETP-C',	'ETP-D',	'ETP-E',	'ETR',	'ETRN',	'ETV',	'ETW',	'ETX',	'ETY',	'EURN',	'EV',	'EVA',	'EVC',	'EVF',	'EVG',	'EVH',	'EVN',	'EVR',	'EVRG',	'EVRI',	'EVT',	'EVTC',	'EW',	'EXD',	'EXG',	'EXK',	'EXP',	'EXPR',	'EXR',	'EXTN',	'EZT',	'F',	'F-B',	'F-C',	'FAF',	'FAM',	'FBC',	'FBHS',	'FBK',	'FBM',	'FBP',	'FC',	'FCAU',	'FCF',	'FCN',	'FCPT',	'FCT',	'FCX',	'FDEU',	'FDP',	'FDS',	'FDX',	'FE',	'FEA.U',	'FEDU',	'FEI',	'FENG',	'FEO',	'FET',	'FF',	'FFA',	'FFC',	'FFG',	'FG',	'FG.W',	'FGB',	'FHI',	'FHN',	'FHN-A',	'FI',	'FICO',	'FIF',	'FINS',	'FINV',	'FIS',	'FIT',	'FIV',	'FIX',	'FL',	'FLC',	'FLNG',	'FLO',	'FLOW',	'FLR',	'FLS',	'FLT',	'FLY',	'FMC',	'FMN',	'FMO',	'FMS',	'FMX',	'FMY',	'FN',	'FNB',	'FNB-E',	'FND',	'FNF',	'FNV',	'FOE',	'FOF',	'FOR',	'FPA.U',	'FPA.W',	'FPAC',	'FPF',	'FPH',	'FPI',	'FPI-B',	'FPL',	'FR',	'FRA',	'FRC',	'FRC-F',	'FRC-G',	'FRC-H',	'FRC-I',	'FRC-J',	'FRO',	'FRT',	'FRT-C',	'FSB',	'FSD',	'FSK',	'FSLY',	'FSM',	'FSS',	'FT',	'FTA-A',	'FTA-B',	'FTAI',	'FTCH',	'FTI',	'FTK',	'FTS',	'FTSI',	'FTV',	'FTV-A',	'FUL',	'FUN',	'FVRR',	'G',	'GAB',	'GAB-G',	'GAB-H',	'GAB-J',	'GAB-K',	'GAM',	'GAM-B',	'GATX',	'GBAB',	'GBL',	'GBX',	'GCAP',	'GCI',	'GCO',	'GCP',	'GCV',	'GD',	'GDDY',	'GDL',	'GDL-C',	'GDO',	'GDOT',	'GDV',	'GDV-A',	'GDV-G',	'GDV-H',	'GE',	'GEF',	'GEF.B',	'GEL',	'GEN',	'GEO',	'GER',	'GES',	'GF',	'GFF',	'GFI',	'GFL',	'GFLU',	'GFY',	'GGB',	'GGG',	'GGM',	'GGT',	'GGT-E',	'GGT-G',	'GGZ',	'GGZ-A',	'GHC',	'GHG',	'GHL',	'GHM',	'GHY',	'GIB',	'GIL',	'GIM',	'GIS',	'GIX',	'GIX.P',	'GIX.U',	'GIX.W',	'GJH',	'GJO',	'GJP',	'GJR',	'GJS',	'GJT',	'GKOS',	'GL',	'GL-C',	'GLE.U',	'GLE.W',	'GLEO',	'GLO-A',	'GLO-B',	'GLO-C',	'GLO-G',	'GLOB',	'GLOG',	'GLOP',	'GLP',	'GLP-A',	'GLT',	'GLW',	'GM',	'GME',	'GMED',	'GMR-A',	'GMRE',	'GMS',	'GMTA',	'GMZ',	'GNC',	'GNE',	'GNE-A',	'GNK',	'GNL',	'GNL-A',	'GNL-B',	'GNRC',	'GNT',	'GNT-A',	'GNW',	'GOF',	'GOL',	'GOLD',	'GOLF',	'GOOS',	'GPC',	'GPI',	'GPJA',	'GPK',	'GPM',	'GPMT',	'GPN',	'GPRK',	'GPS',	'GPX',	'GRA',	'GRA.U',	'GRA.W',	'GRAF',	'GRAM',	'GRC',	'GRP.U',	'GRUB',	'GRX',	'GRX-A',	'GRX-B',	'GS',	'GS-A',	'GS-C',	'GS-D',	'GS-J',	'GS-K',	'GS-N',	'GSBD',	'GSH',	'GSK',	'GSL',	'GSL-B',	'GSLD',	'GSX',	'GTES',	'GTN',	'GTN.A',	'GTS',	'GTT',	'GTX',	'GTY',	'GUT',	'GUT-A',	'GUT-C',	'GVA',	'GWB',	'GWRE',	'GWW',	'GYC',	'H',	'HAE',	'HAL',	'HASI',	'HBB',	'HBI',	'HBM',	'HCA',	'HCC',	'HCFT',	'HCHC',	'HCI',	'HCR',	'HCXY',	'HCXZ',	'HD',	'HDB',	'HE',	'HEI',	'HEI.A',	'HEP',	'HEQ',	'HES',	'HESM',	'HEXO',	'HFC',	'HFR-A',	'HFRO',	'HGH',	'HGLB',	'HGV',	'HHC',	'HHS',	'HI',	'HIE',	'HIG',	'HIG-G',	'HII',	'HIL',	'HIO',	'HIW',	'HIX',	'HJV',	'HKIB',	'HL',	'HL-B',	'HLF',	'HLI',	'HLT',	'HLX',	'HMC',	'HMI',	'HML-A',	'HMLP',	'HMN',	'HMY',	'HNGR',	'HNI',	'HNP',	'HOG',	'HOME',	'HON',	'HOV',	'HP',	'HPE',	'HPF',	'HPI',	'HPP',	'HPQ',	'HPR',	'HPS',	'HQH',	'HQL',	'HR',	'HRB',	'HRC',	'HRI',	'HRL',	'HRTG',	'HSB-A',	'HSBC',	'HSC',	'HST',	'HSY',	'HT',	'HT-C',	'HT-D',	'HT-E',	'HTA',	'HTD',	'HTFA',	'HTGC',	'HTH',	'HTY',	'HTZ',	'HUBB',	'HUBS',	'HUD',	'HUM',	'HUN',	'HUYA',	'HVT',	'HVT.A',	'HWM',	'HXL',	'HY',	'HYB',	'HYI',	'HYT',	'HZN',	'HZO',	'I',	'IAA',	'IAE',	'IAG',	'IBA',	'IBM',	'IBN',	'IBP',	'ICD',	'ICE',	'ICL',	'IDA',	'IDE',	'IDT',	'IEX',	'IFF',	'IFFT',	'IFN',	'IFS',	'IGA',	'IGD',	'IGI',	'IGR',	'IGT',	'IHC',	'IHD',	'IHG',	'IHIT',	'IHTA',	'IID',	'IIF',	'IIM',	'IIP-A',	'IIPR',	'IMAX',	'INFO',	'INFY',	'ING',	'INGR',	'INN',	'INN-D',	'INN-E',	'INS-A',	'INSI',	'INSP',	'INST',	'INSW',	'INT',	'INVH',	'INXN',	'IO',	'IP',	'IPG',	'IPHI',	'IPI',	'IPV',	'IPV.U',	'IPV.W',	'IQI',	'IQV',	'IR',	'IRE-C',	'IRET',	'IRL',	'IRM',	'IRR',	'IRS',	'IRT',	'ISD',	'ISG',	'IT',	'ITCB',	'ITGR',	'ITT',	'ITUB',	'ITW',	'IVC',	'IVH',	'IVR',	'IVR-A',	'IVR-B',	'IVR-C',	'IVZ',	'IX',	'J',	'JAX',	'JBGS',	'JBK',	'JBL',	'JBN',	'JBR',	'JBT',	'JCA-B',	'JCAP',	'JCE',	'JCI',	'JCO',	'JCP',	'JDD',	'JE',	'JE-A',	'JEF',	'JELD',	'JEMD',	'JEQ',	'JFR',	'JGH',	'JHAA',	'JHB',	'JHG',	'JHI',	'JHS',	'JHX',	'JHY',	'JIH',	'JIH.U',	'JIH.W',	'JILL',	'JKS',	'JLL',	'JLS',	'JMEI',	'JMF',	'JMIA',	'JMLP',	'JMM',	'JMP',	'JNJ',	'JNPR',	'JOE',	'JOF',	'JP',	'JPC',	'JPI',	'JPM',	'JPM-C',	'JPM-D',	'JPM-G',	'JPM-H',	'JPM-J',	'JPS',	'JPT',	'JQC',	'JRI',	'JRO',	'JRS',	'JSD',	'JT',	'JTA',	'JTD',	'JW.A',	'JW.B',	'JWN',	'K',	'KAI',	'KAMN',	'KAR',	'KB',	'KBH',	'KBR',	'KDMN',	'KDP',	'KEM',	'KEN',	'KEP',	'KEX',	'KEY',	'KEY-I',	'KEY-J',	'KEY-K',	'KEYS',	'KF',	'KFS',	'KFY',	'KGC',	'KIM',	'KIM-L',	'KIM-M',	'KIO',	'KKR',	'KKR-A',	'KKR-B',	'KL',	'KMB',	'KMF',	'KMI',	'KMPR',	'KMT',	'KMX',	'KN',	'KNL',	'KNOP',	'KNX',	'KO',	'KODK',	'KOF',	'KOP',	'KOS',	'KR',	'KRA',	'KRC',	'KREF',	'KRG',	'KRO',	'KRP',	'KSM',	'KSS',	'KSU',	'KSU.P',	'KT',	'KTB',	'KTF',	'KTH',	'KTN',	'KTP',	'KW',	'KWR',	'KYN',	'L',	'LAC',	'LAD',	'LADR',	'LAIX',	'LAZ',	'LB',	'LBRT',	'LC',	'LCI',	'LCII',	'LDL',	'LDOS',	'LDP',	'LEA',	'LEAF',	'LEE',	'LEG',	'LEJU',	'LEN',	'LEN.B',	'LEO',	'LEVI',	'LFC',	'LGC',	'LGC.U',	'LGC.W',	'LGF.A',	'LGF.B',	'LGI',	'LH',	'LHC',	'LHC.U',	'LHC.W',	'LHX',	'LII',	'LIN',	'LINX',	'LITB',	'LL',	'LLY',	'LM',	'LMHA',	'LMHB',	'LMT',	'LN',	'LNC',	'LND',	'LNN',	'LOMA',	'LOW',	'LPG',	'LPI',	'LPL',	'LPX',	'LRN',	'LSI',	'LTC',	'LTHM',	'LTM',	'LUB',	'LUV',	'LVS',	'LW',	'LXFR',	'LXP',	'LXP-C',	'LXU',	'LYB',	'LYG',	'LYV',	'LZB',	'M',	'MA',	'MAA',	'MAA-I',	'MAC',	'MAIN',	'MAN',	'MANU',	'MAS',	'MATX',	'MAV',	'MAXR',	'MBI',	'MBT',	'MC',	'MCA',	'MCB',	'MCC',	'MCD',	'MCI',	'MCK',	'MCN',	'MCO',	'MCR',	'MCS',	'MCV',	'MCX',	'MCY',	'MD',	'MDC',	'MDLA',	'MDLQ',	'MDLX',	'MDLY',	'MDP',	'MDT',	'MDU',	'MEC',	'MED',	'MEI',	'MEN',	'MER-K',	'MET',	'MET-A',	'MET-E',	'MET-F',	'MFA',	'MFA-B',	'MFA-C',	'MFA.U',	'MFA.W',	'MFAC',	'MFC',	'MFD',	'MFG',	'MFGP',	'MFL',	'MFM',	'MFO',	'MFT',	'MFV',	'MG',	'MGA',	'MGF',	'MGM',	'MGP',	'MGR',	'MGU',	'MGY',	'MH-A',	'MH-C',	'MH-D',	'MHD',	'MHE',	'MHF',	'MHI',	'MHK',	'MHLA',	'MHN',	'MHNC',	'MHO',	'MIC',	'MIE',	'MIN',	'MIT-A',	'MIT-B',	'MIT-C',	'MITT',	'MIXT',	'MIY',	'MKC',	'MKC.V',	'MKL',	'MLI',	'MLM',	'MLP',	'MLR',	'MMC',	'MMD',	'MMI',	'MMM',	'MMP',	'MMS',	'MMT',	'MMU',	'MN',	'MNE',	'MNK',	'MNP',	'MNR',	'MNR-C',	'MNRL',	'MO',	'MOD',	'MODN',	'MOG.A',	'MOG.B',	'MOGU',	'MOH',	'MOS',	'MOV',	'MPA',	'MPC',	'MPLX',	'MPV',	'MPW',	'MPX',	'MQT',	'MQY',	'MR',	'MRC',	'MRK',	'MRO',	'MS',	'MS-A',	'MS-E',	'MS-F',	'MS-I',	'MS-K',	'MS-L',	'MSA',	'MSB',	'MSC',	'MSCI',	'MSD',	'MSG',	'MSGN',	'MSI',	'MSM',	'MT',	'MTB',	'MTD',	'MTDR',	'MTG',	'MTH',	'MTL',	'MTL.P',	'MTN',	'MTOR',	'MTR',	'MTRN',	'MTT',	'MTW',	'MTX',	'MTZ',	'MUA',	'MUC',	'MUE',	'MUFG',	'MUH',	'MUI',	'MUJ',	'MUR',	'MUS',	'MUSA',	'MUX',	'MVC',	'MVCD',	'MVF',	'MVO',	'MVT',	'MWA',	'MX',	'MXE',	'MXF',	'MXL',	'MYC',	'MYD',	'MYE',	'MYF',	'MYI',	'MYJ',	'MYN',	'MYOV',	'MZA',	'NAC',	'NAD',	'NAN',	'NAT',	'NAV',	'NAV-D',	'NAZ',	'NBB',	'NBHC',	'NBR',	'NBR-A',	'NC',	'NCA',	'NCB',	'NCLH',	'NCR',	'NCV',	'NCV-A',	'NCZ',	'NCZ-A',	'NDP',	'NE',	'NEA',	'NEE',	'NEE-I',	'NEE-J',	'NEE-K',	'NEE-N',	'NEE-O',	'NEE-P',	'NEM',	'NEP',	'NET',	'NEU',	'NEV',	'NEW',	'NEWR',	'NEX',	'NEXA',	'NFG',	'NFH',	'NFH.W',	'NFJ',	'NGG',	'NGL',	'NGL-A',	'NGL-B',	'NGL-C',	'NGS',	'NGVC',	'NGVT',	'NHA',	'NHF',	'NHI',	'NI',	'NI-B',	'NID',	'NIE',	'NIM',	'NINE',	'NIO',	'NIQ',	'NJR',	'NJV',	'NKE',	'NKG',	'NKX',	'NL',	'NLS',	'NLSN',	'NLY',	'NLY-D',	'NLY-F',	'NLY-G',	'NLY-I',	'NM',	'NM-G',	'NM-H',	'NMCO',	'NMFC',	'NMFX',	'NMI',	'NMK-B',	'NMK-C',	'NMM',	'NMR',	'NMS',	'NMT',	'NMY',	'NMZ',	'NNA',	'NNI',	'NNN',	'NNN-F',	'NNY',	'NOA',	'NOAH',	'NOC',	'NOK',	'NOM',	'NOMD',	'NOV',	'NOVA',	'NOW',	'NP',	'NPK',	'NPN',	'NPO',	'NPTN',	'NPV',	'NQP',	'NR',	'NREF',	'NRG',	'NRGX',	'NRK',	'NRP',	'NRT',	'NRUC',	'NRZ',	'NRZ-A',	'NRZ-B',	'NRZ-C',	'NS',	'NS-A',	'NS-B',	'NS-C',	'NSA',	'NSA-A',	'NSC',	'NSC.W',	'NSCO',	'NSL',	'NSP',	'NSS',	'NTB',	'NTCO',	'NTEST.I',	'NTEST.J',	'NTEST.K',	'NTG',	'NTP',	'NTR',	'NTZ',	'NUE',	'NUM',	'NUO',	'NUS',	'NUV',	'NUW',	'NVG',	'NVGS',	'NVO',	'NVR',	'NVRO',	'NVS',	'NVST',	'NVT',	'NVTA',	'NWE',	'NWHM',	'NWN',	'NX',	'NXC',	'NXJ',	'NXN',	'NXP',	'NXQ',	'NXR',	'NXRT',	'NYC-A',	'NYC-U',	'NYCB',	'NYT',	'NYV',	'NZF',	'O',	'OAC',	'OAC.U',	'OAC.W',	'OAK-A',	'OAK-B',	'OBE',	'OC',	'OCFT',	'OCN',	'ODC',	'OEC',	'OFC',	'OFG',	'OFG-A',	'OFG-B',	'OFG-D',	'OGE',	'OGS',	'OHI',	'OI',	'OIA',	'OIB.C',	'OII',	'OIS',	'OKE',	'OLN',	'OLP',	'OMC',	'OMF',	'OMI',	'OMN',	'ONDK',	'ONE',	'ONTO',	'OOMA',	'OPP',	'OPY',	'OR',	'ORA',	'ORAN',	'ORC',	'ORCC',	'ORCL',	'ORI',	'ORN',	'OSB',	'OSG',	'OSK',	'OTI.P',	'OUT',	'OVV',	'OXM',	'OXY',	'PAA',	'PAC',	'PAC.W',	'PACD',	'PACK',	'PAG',	'PAGP',	'PAGS',	'PAI',	'PAM',	'PANW',	'PAR',	'PARR',	'PAYC',	'PB',	'PBA',	'PBB',	'PBC',	'PBF',	'PBFX',	'PBH',	'PBI',	'PBI-B',	'PBR',	'PBR.A',	'PBT',	'PBY',	'PCF',	'PCG',	'PCI',	'PCK',	'PCM',	'PCN',	'PCQ',	'PD',	'PDI',	'PDM',	'PDS',	'PDT',	'PE',	'PEAK',	'PEB',	'PEB-C',	'PEB-D',	'PEB-E',	'PEB-F',	'PEG',	'PEI',	'PEI-B',	'PEI-C',	'PEI-D',	'PEN',	'PEO',	'PER',	'PFD',	'PFE',	'PFGC',	'PFH',	'PFL',	'PFN',	'PFO',	'PFS',	'PFSI',	'PG',	'PGP',	'PGR',	'PGRE',	'PGTI',	'PGZ',	'PH',	'PHD',	'PHG',	'PHI',	'PHK',	'PHM',	'PHR',	'PHT',	'PHX',	'PIC',	'PIC.U',	'PIC.W',	'PII',	'PIM',	'PINE',	'PING',	'PINS',	'PIPR',	'PIY',	'PJH',	'PJT',	'PK',	'PKE',	'PKG',	'PKI',	'PKO',	'PKX',	'PLAN',	'PLD',	'PLNT',	'PLOW',	'PLT',	'PLYM',	'PM',	'PMF',	'PML',	'PMM',	'PMO',	'PMT',	'PMT-A',	'PMT-B',	'PMX',	'PNC',	'PNC-P',	'PNC-Q',	'PNF',	'PNI',	'PNM',	'PNR',	'PNW',	'POL',	'POR',	'POST',	'PPG',	'PPL',	'PPR',	'PPT',	'PPX',	'PQG',	'PRA',	'PRE-F',	'PRE-G',	'PRE-H',	'PRE-I',	'PRGO',	'PRH',	'PRI',	'PRI-A',	'PRI-B',	'PRI-C',	'PRI-D',	'PRI-E',	'PRI-F',	'PRLB',	'PRMW',	'PRO',	'PROS',	'PRS',	'PRSP',	'PRT',	'PRTY',	'PRU',	'PSA',	'PSA-B',	'PSA-C',	'PSA-D',	'PSA-E',	'PSA-F',	'PSA-G',	'PSA-H',	'PSA-I',	'PSA-J',	'PSA-K',	'PSA-V',	'PSA-W',	'PSA-X',	'PSB',	'PSB-W',	'PSB-X',	'PSB-Y',	'PSB-Z',	'PSF',	'PSN',	'PSO',	'PSTG',	'PSTL',	'PSV',	'PSX',	'PSXP',	'PTR',	'PTY',	'PUK',	'PUK-A',	'PUK.P',	'PUMP',	'PVG',	'PVH',	'PVL',	'PWR',	'PXD',	'PYN',	'PYS',	'PYT',	'PYX',	'PZC',	'PZN',	'QD',	'QEP',	'QES',	'QGEN',	'QHC',	'QSR',	'QTS',	'QTS-A',	'QTS-B',	'QTWO',	'QUAD',	'QUOT',	'QVCC',	'QVCD',	'R',	'RA',	'RACE',	'RAD',	'RAMP',	'RBA',	'RBC',	'RBS',	'RC',	'RCA',	'RCB',	'RCI',	'RCL',	'RCP',	'RCS',	'RCUS',	'RDN',	'RDS.A',	'RDS.B',	'RDY',	'RE',	'RELX',	'RENN',	'RES',	'RESI',	'REV',	'REVG',	'REX',	'REX-A',	'REX-B',	'REX-C',	'REXR',	'REZI',	'RF',	'RF-A',	'RF-B',	'RF-C',	'RFI',	'RFL',	'RFM',	'RFP',	'RGA',	'RGR',	'RGS',	'RGT',	'RH',	'RHI',	'RHP',	'RIG',	'RIO',	'RIV',	'RJF',	'RL',	'RLGY',	'RLH',	'RLI',	'RLJ',	'RLJ-A',	'RM',	'RMAX',	'RMD',	'RMED',	'RMG',	'RMG.U',	'RMG.W',	'RMI',	'RMM',	'RMP.P',	'RMT',	'RNG',	'RNGR',	'RNP',	'RNR',	'RNR-C',	'RNR-E',	'RNR-F',	'ROG',	'ROK',	'ROL',	'ROP',	'ROYT',	'RPAI',	'RPL.U',	'RPL.W',	'RPLA',	'RPM',	'RPT',	'RPT-D',	'RQI',	'RRC',	'RRD',	'RRTS',	'RS',	'RSF',	'RSG',	'RST',	'RTN',	'RTW',	'RUBI',	'RVI',	'RVLV',	'RVT',	'RWT',	'RXN',	'RY',	'RY-T',	'RYAM',	'RYB',	'RYCE',	'RYI',	'RYN',	'RZA',	'RZB',	'S',	'SA',	'SAF',	'SAFE',	'SAH',	'SAIC',	'SAIL',	'SALT',	'SAM',	'SAN',	'SAN-B',	'SAND',	'SAP',	'SAR',	'SAVE',	'SB',	'SB-C',	'SB-D',	'SBE',	'SBE.U',	'SBE.W',	'SBH',	'SBI',	'SBNA',	'SBOW',	'SBR',	'SBS',	'SBSW',	'SC',	'SCA',	'SCCO',	'SCD',	'SCE-G',	'SCE-H',	'SCE-J',	'SCE-K',	'SCE-L',	'SCH-C',	'SCH-D',	'SCHW',	'SCI',	'SCL',	'SCM',	'SCP.U',	'SCP.W',	'SCPE',	'SCS',	'SCU',	'SCV.U',	'SCV.W',	'SCVX',	'SCX',	'SD',	'SDRL',	'SE',	'SEAS',	'SEE',	'SEM',	'SERV',	'SF',	'SF-A',	'SF-B',	'SFB',	'SFE',	'SFL',	'SFT.U',	'SFT.W',	'SFTW',	'SFUN',	'SGU',	'SHAK',	'SHG',	'SHI',	'SHL.U',	'SHL.W',	'SHLL',	'SHLX',	'SHO',	'SHO-E',	'SHO-F',	'SHOP',	'SHW',	'SI',	'SID',	'SIG',	'SIT-A',	'SIT-K',	'SITC',	'SITE',	'SIX',	'SJI',	'SJIJ',	'SJIU',	'SJM',	'SJR',	'SJT',	'SJW',	'SKM',	'SKT',	'SKX',	'SKY',	'SLB',	'SLCA',	'SLF',	'SLG',	'SLG-I',	'SM',	'SMAR',	'SMFG',	'SMG',	'SMHI',	'SMLP',	'SMM',	'SMP',	'SNA',	'SNAP',	'SNDR',	'SNE',	'SNN',	'SNP',	'SNR',	'SNV',	'SNV-D',	'SNV-E',	'SNX',	'SO',	'SOGO',	'SOI',	'SOJA',	'SOJB',	'SOJC',	'SOJD',	'SOL',	'SOLN',	'SON',	'SOR',	'SPA.U',	'SPA.W',	'SPAQ',	'SPB',	'SPC.U',	'SPC.W',	'SPCE',	'SPE',	'SPE-B',	'SPG',	'SPG-J',	'SPGI',	'SPH',	'SPL-A',	'SPLP',	'SPN',	'SPOT',	'SPR',	'SPXC',	'SPXX',	'SQ',	'SQM',	'SQNS',	'SR',	'SR-A',	'SRC',	'SRC-A',	'SRE',	'SRE-A',	'SRE-B',	'SREA',	'SRF',	'SRG',	'SRG-A',	'SRI',	'SRL',	'SRLP',	'SRT',	'SRV',	'SSD',	'SSI',	'SSL',	'SSTK',	'SSWA',	'ST',	'STA-C',	'STA-D',	'STA-G',	'STA-I',	'STAG',	'STAR',	'STC',	'STE',	'STG',	'STK',	'STL',	'STL-A',	'STM',	'STN',	'STNG',	'STON',	'STOR',	'STT',	'STT-C',	'STT-D',	'STT-G',	'STWD',	'STZ',	'STZ.B',	'SU',	'SUI',	'SUM',	'SUN',	'SUP',	'SUPV',	'SUZ',	'SWCH',	'SWI',	'SWK',	'SWM',	'SWN',	'SWP',	'SWT',	'SWX',	'SWZ',	'SXC',	'SXI',	'SXT',	'SYF',	'SYF-A',	'SYK',	'SYX',	'SYY',	'SZC',	'T',	'T-A',	'T-C',	'TAC',	'TAK',	'TAL',	'TALO',	'TAP',	'TAP.A',	'TARO',	'TBB',	'TBC',	'TBI',	'TCI',	'TCO',	'TCO-J',	'TCO-K',	'TCP',	'TCRW',	'TCRZ',	'TCS',	'TD',	'TDA',	'TDC',	'TDE',	'TDF',	'TDG',	'TDI',	'TDJ',	'TDOC',	'TDS',	'TDW',	'TDW.A',	'TDW.B',	'TDY',	'TEAF',	'TECK',	'TEF',	'TEI',	'TEL',	'TEN',	'TEO',	'TEVA',	'TEX',	'TFC',	'TFC-F',	'TFC-G',	'TFC-H',	'TFC-I',	'TFII',	'TFX',	'TG',	'TGE',	'TGH',	'TGI',	'TGNA',	'TGP',	'TGP-A',	'TGP-B',	'TGS',	'TGT',	'THC',	'THG',	'THGA',	'THO',	'THQ',	'THR',	'THS',	'THW',	'TIF',	'TISI',	'TJX',	'TK',	'TKC',	'TKR',	'TLI',	'TLK',	'TLRA',	'TLRD',	'TLYS',	'TM',	'TME',	'TMHC',	'TMO',	'TMST',	'TNC',	'TNET',	'TNK',	'TNP',	'TNP-C',	'TNP-D',	'TNP-E',	'TNP-F',	'TOL',	'TOO-A',	'TOO-B',	'TOO-E',	'TOT',	'TPB',	'TPC',	'TPH',	'TPL',	'TPR',	'TPRE',	'TPVG',	'TPVY',	'TPX',	'TPZ',	'TR',	'TRC',	'TREC',	'TREX',	'TRGP',	'TRI',	'TRN',	'TRN.U',	'TRN.W',	'TRNE',	'TRNO',	'TROX',	'TRP',	'TRQ',	'TRT-A',	'TRT-B',	'TRT-C',	'TRT-D',	'TRTN',	'TRTX',	'TRU',	'TRV',	'TRWH',	'TS',	'TSE',	'TSI',	'TSLF',	'TSLX',	'TSM',	'TSN',	'TSQ',	'TSU',	'TT',	'TTC',	'TTI',	'TTM',	'TTP',	'TU',	'TUFN',	'TUP',	'TV',	'TVC',	'TVE',	'TWI',	'TWLO',	'TWN',	'TWO',	'TWO-A',	'TWO-B',	'TWO-C',	'TWO-D',	'TWO-E',	'TWTR',	'TX',	'TXT',	'TY',	'TY.P',	'TYG',	'TYL',	'UA',	'UAA',	'UAN',	'UBA',	'UBER',	'UBP',	'UBP-H',	'UBP-K',	'UBS',	'UDR',	'UE',	'UFI',	'UFS',	'UGI',	'UGP',	'UHS',	'UHT',	'UI',	'UIS',	'UL',	'UMC',	'UMH',	'UMH-B',	'UMH-C',	'UMH-D',	'UN',	'UNF',	'UNFI',	'UNH',	'UNM',	'UNMA',	'UNP',	'UNT',	'UNVR',	'UPS',	'URI',	'USA',	'USAC',	'USB',	'USB-A',	'USB-H',	'USB-M',	'USB-O',	'USB-P',	'USDP',	'USFD',	'USM',	'USNA',	'USPH',	'USX',	'UTF',	'UTI',	'UTL',	'UTX',	'UTX.P',	'UVE',	'UVV',	'UZA',	'UZB',	'UZC',	'V',	'VAC',	'VAL',	'VALE',	'VAM',	'VAPO',	'VAR',	'VBF',	'VCIF',	'VCRA',	'VCV',	'VEC',	'VEDL',	'VEEV',	'VEL',	'VER',	'VER-F',	'VER.U',	'VET',	'VFC',	'VGI',	'VGM',	'VGR',	'VHI',	'VICI',	'VIPS',	'VIST',	'VIV',	'VJET',	'VKQ',	'VLO',	'VLRS',	'VLT',	'VMC',	'VMI',	'VMO',	'VMW',	'VNCE',	'VNE',	'VNO',	'VNO-K',	'VNO-L',	'VNO-M',	'VNTR',	'VOC',	'VOY-B',	'VOYA',	'VPG',	'VPV',	'VRS',	'VRT',	'VRT.W',	'VRTV',	'VSH',	'VSLR',	'VST',	'VST.A',	'VSTO',	'VTA',	'VTN',	'VTR',	'VVI',	'VVN.W',	'VVNT',	'VVR',	'VVV',	'VZ',	'W',	'WAAS',	'WAB',	'WAL',	'WALA',	'WAT',	'WBAI',	'WBC',	'WBK',	'WBS',	'WBS-F',	'WBT',	'WCC',	'WCN',	'WD',	'WDR',	'WEA',	'WEC',	'WEI',	'WELL',	'WES',	'WEX',	'WF',	'WFC',	'WFC-L',	'WFC-N',	'WFC-O',	'WFC-P',	'WFC-Q',	'WFC-R',	'WFC-T',	'WFC-V',	'WFC-W',	'WFC-X',	'WFC-Y',	'WFC-Z',	'WGO',	'WH',	'WHD',	'WHG',	'WHR',	'WIA',	'WIT',	'WIW',	'WK',	'WLK',	'WLKP',	'WLL',	'WM',	'WMB',	'WMC',	'WMK',	'WMS',	'WMT',	'WNC',	'WNS',	'WOR',	'WORK',	'WOW',	'WPC',	'WPG',	'WPG-H',	'WPG-I',	'WPM',	'WPP',	'WPX',	'WRB',	'WRB-B',	'WRB-C',	'WRB-D',	'WRB-E',	'WRB-F',	'WRE',	'WRI',	'WRK',	'WSM',	'WSO',	'WSO.B',	'WSR',	'WST',	'WTI',	'WTM',	'WTRG',	'WTRU',	'WTS',	'WTTR',	'WU',	'WUBA',	'WWE',	'WWW',	'WY',	'WYND',	'X',	'XAN',	'XAN-C',	'XEC',	'XFLT',	'XHR',	'XIN',	'XOM',	'XPO',	'XRF',	'XRX',	'XYF',	'XYL',	'Y',	'YELP',	'YETI',	'YEXT',	'YPF',	'YRD',	'YUM',	'YUMC',	'ZBH',	'ZEN',	'ZNH',	'ZTO',	'ZTR',	'ZTS',	'ZUO',	'ZYME', ]
    # Format the allStocks variable for use in the class.
    self.allStocks = []
    for stock in stockUniverse:
      self.allStocks.append([stock, 0])

    self.long = []
    self.short = []
    self.qShort = None
    self.qLong = None
    self.adjustedQLong = None
    self.adjustedQShort = None
    self.blacklist = set()
    self.longAmount = 0
    self.shortAmount = 0
    self.timeToClose = None

  def run(self):
    # First, cancel any existing orders so they don't impact our buying power.
    orders = self.alpaca.list_orders(status="open")
    for order in orders:
      self.alpaca.cancel_order(order.id)

    # Wait for market to open.
    print("Waiting for market to open...")
    tAMO = threading.Thread(target=self.awaitMarketOpen)
    tAMO.start()
    tAMO.join()
    print("Market opened.")

    # Rebalance the portfolio every minute, making necessary trades.
    while True:

      # Figure out when the market will close so we can prepare to sell beforehand.
      clock = self.alpaca.get_clock()
      closingTime = clock.next_close.replace(tzinfo=datetime.timezone.utc).timestamp()
      currTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
      self.timeToClose = closingTime - currTime

      if(self.timeToClose < (60 * 15)):
        # Close all positions when 15 minutes til market close.
        print("Market closing soon.  Closing positions.")

        positions = self.alpaca.list_positions()
        for position in positions:
          if(position.side == 'long'):
            orderSide = 'sell'
          else:
            orderSide = 'buy'
          qty = abs(int(float(position.qty)))
          respSO = []
          tSubmitOrder = threading.Thread(target=self.submitOrder(qty, position.symbol, orderSide, respSO))
          tSubmitOrder.start()
          tSubmitOrder.join()

        # Run script again after market close for next trading day.
        print("Sleeping until market close (15 minutes).")
        time.sleep(60 * 15)
      else:
        # Rebalance the portfolio.
        tRebalance = threading.Thread(target=self.rebalance)
        tRebalance.start()
        tRebalance.join()
        time.sleep(60)

  # Wait for market to open.
  def awaitMarketOpen(self):
    isOpen = self.alpaca.get_clock().is_open
    while(not isOpen):
      clock = self.alpaca.get_clock()
      openingTime = clock.next_open.replace(tzinfo=datetime.timezone.utc).timestamp()
      currTime = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
      timeToOpen = int((openingTime - currTime) / 60)
      print(str(timeToOpen) + " minutes til market open.")
      time.sleep(60)
      isOpen = self.alpaca.get_clock().is_open

  def rebalance(self):
    tRerank = threading.Thread(target=self.rerank)
    tRerank.start()
    tRerank.join()

    # Clear existing orders again.
    orders = self.alpaca.list_orders(status="open")
    for order in orders:
      self.alpaca.cancel_order(order.id)

    print("We are taking a long position in: " + str(self.long))
    print("We are taking a short position in: " + str(self.short))
    # Remove positions that are no longer in the short or long list, and make a list of positions that do not need to change.  Adjust position quantities if needed.
    executed = [[], []]
    positions = self.alpaca.list_positions()
    self.blacklist.clear()
    for position in positions:
      if(self.long.count(position.symbol) == 0):
        # Position is not in long list.
        if(self.short.count(position.symbol) == 0):
          # Position not in short list either.  Clear position.
          if(position.side == "long"):
            side = "sell"
          else:
            side = "buy"
          respSO = []
          tSO = threading.Thread(target=self.submitOrder, args=[abs(int(float(position.qty))), position.symbol, side, respSO])
          tSO.start()
          tSO.join()
        else:
          # Position in short list.
          if(position.side == "long"):
            # Position changed from long to short.  Clear long position to prepare for short position.
            side = "sell"
            respSO = []
            tSO = threading.Thread(target=self.submitOrder, args=[int(float(position.qty)), position.symbol, side, respSO])
            tSO.start()
            tSO.join()
          else:
            if(abs(int(float(position.qty))) == self.qShort):
              # Position is where we want it.  Pass for now.
              pass
            else:
              # Need to adjust position amount
              diff = abs(int(float(position.qty))) - self.qShort
              if(diff > 0):
                # Too many short positions.  Buy some back to rebalance.
                side = "buy"
              else:
                # Too little short positions.  Sell some more.
                side = "sell"
              respSO = []
              tSO = threading.Thread(target=self.submitOrder, args=[abs(diff), position.symbol, side, respSO])
              tSO.start()
              tSO.join()
            executed[1].append(position.symbol)
            self.blacklist.add(position.symbol)
      else:
        # Position in long list.
        if(position.side == "short"):
          # Position changed from short to long.  Clear short position to prepare for long position.
          respSO = []
          tSO = threading.Thread(target=self.submitOrder, args=[abs(int(float(position.qty))), position.symbol, "buy", respSO])
          tSO.start()
          tSO.join()
        else:
          if(int(float(position.qty)) == self.qLong):
            # Position is where we want it.  Pass for now.
            pass
          else:
            # Need to adjust position amount.
            diff = abs(int(float(position.qty))) - self.qLong
            if(diff > 0):
              # Too many long positions.  Sell some to rebalance.
              side = "sell"
            else:
              # Too little long positions.  Buy some more.
              side = "buy"
            respSO = []
            tSO = threading.Thread(target=self.submitOrder, args=[abs(diff), position.symbol, side, respSO])
            tSO.start()
            tSO.join()
          executed[0].append(position.symbol)
          self.blacklist.add(position.symbol)

    # Send orders to all remaining stocks in the long and short list.
    respSendBOLong = []
    tSendBOLong = threading.Thread(target=self.sendBatchOrder, args=[self.qLong, self.long, "buy", respSendBOLong])
    tSendBOLong.start()
    tSendBOLong.join()
    respSendBOLong[0][0] += executed[0]
    if(len(respSendBOLong[0][1]) > 0):
      # Handle rejected/incomplete orders and determine new quantities to purchase.
      respGetTPLong = []
      tGetTPLong = threading.Thread(target=self.getTotalPrice, args=[respSendBOLong[0][0], respGetTPLong])
      tGetTPLong.start()
      tGetTPLong.join()
      if (respGetTPLong[0] > 0):
        self.adjustedQLong = self.longAmount // respGetTPLong[0]
      else:
        self.adjustedQLong = -1
    else:
      self.adjustedQLong = -1

    respSendBOShort = []
    tSendBOShort = threading.Thread(target=self.sendBatchOrder, args=[self.qShort, self.short, "sell", respSendBOShort])
    tSendBOShort.start()
    tSendBOShort.join()
    respSendBOShort[0][0] += executed[1]
    if(len(respSendBOShort[0][1]) > 0):
      # Handle rejected/incomplete orders and determine new quantities to purchase.
      respGetTPShort = []
      tGetTPShort = threading.Thread(target=self.getTotalPrice, args=[respSendBOShort[0][0], respGetTPShort])
      tGetTPShort.start()
      tGetTPShort.join()
      if(respGetTPShort[0] > 0):
        self.adjustedQShort = self.shortAmount // respGetTPShort[0]
      else:
        self.adjustedQShort = -1
    else:
      self.adjustedQShort = -1

    # Reorder stocks that didn't throw an error so that the equity quota is reached.
    if(self.adjustedQLong > -1):
      self.qLong = int(self.adjustedQLong - self.qLong)
      for stock in respSendBOLong[0][0]:
        respResendBOLong = []
        tResendBOLong = threading.Thread(target=self.submitOrder, args=[self.qLong, stock, "buy", respResendBOLong])
        tResendBOLong.start()
        tResendBOLong.join()

    if(self.adjustedQShort > -1):
      self.qShort = int(self.adjustedQShort - self.qShort)
      for stock in respSendBOShort[0][0]:
        respResendBOShort = []
        tResendBOShort = threading.Thread(target=self.submitOrder, args=[self.qShort, stock, "sell", respResendBOShort])
        tResendBOShort.start()
        tResendBOShort.join()

  # Re-rank all stocks to adjust longs and shorts.
  def rerank(self):
    tRank = threading.Thread(target=self.rank)
    tRank.start()
    tRank.join()

    # Grabs the top and bottom quarter of the sorted stock list to get the long and short lists.
    longShortAmount = len(self.allStocks) // 4
    self.long = []
    self.short = []
    for i, stockField in enumerate(self.allStocks):
      if(i < longShortAmount):
        self.short.append(stockField[0])
      elif(i > (len(self.allStocks) - 1 - longShortAmount)):
        self.long.append(stockField[0])
      else:
        continue

    # Determine amount to long/short based on total stock price of each bucket.
    equity = int(float(self.alpaca.get_account().equity))

    self.shortAmount = equity * 0.30
    self.longAmount = equity + self.shortAmount

    respGetTPLong = []
    tGetTPLong = threading.Thread(target=self.getTotalPrice, args=[self.long, respGetTPLong])
    tGetTPLong.start()
    tGetTPLong.join()

    respGetTPShort = []
    tGetTPShort = threading.Thread(target=self.getTotalPrice, args=[self.short, respGetTPShort])
    tGetTPShort.start()
    tGetTPShort.join()

    self.qLong = int(self.longAmount // respGetTPLong[0])
    self.qShort = int(self.shortAmount // respGetTPShort[0])

  # Get the total price of the array of input stocks.
  def getTotalPrice(self, stocks, resp):
    totalPrice = 0
    for stock in stocks:
      bars = self.alpaca.get_barset(stock, "minute", 1)
      totalPrice += bars[stock][0].c
    resp.append(totalPrice)

  # Submit a batch order that returns completed and uncompleted orders.
  def sendBatchOrder(self, qty, stocks, side, resp):
    executed = []
    incomplete = []
    for stock in stocks:
      if(self.blacklist.isdisjoint({stock})):
        respSO = []
        tSubmitOrder = threading.Thread(target=self.submitOrder, args=[qty, stock, side, respSO])
        tSubmitOrder.start()
        tSubmitOrder.join()
        if(not respSO[0]):
          # Stock order did not go through, add it to incomplete.
          incomplete.append(stock)
        else:
          executed.append(stock)
        respSO.clear()
    resp.append([executed, incomplete])

  # Submit an order if quantity is above 0.
  def submitOrder(self, qty, stock, side, resp):
    if(qty > 0):
      try:
        self.alpaca.submit_order(stock, qty, side, "market", "day")
        print("Market order of | " + str(qty) + " " + stock + " " + side + " | completed.")
        resp.append(True)
      except:
        print("Order of | " + str(qty) + " " + stock + " " + side + " | did not go through.")
        resp.append(False)
    else:
      print("Quantity is 0, order of | " + str(qty) + " " + stock + " " + side + " | not completed.")
      resp.append(True)

  # Get percent changes of the stock prices over the past 10 minutes.
  def getPercentChanges(self):
    length = 10
    for i, stock in enumerate(self.allStocks):
      bars = self.alpaca.get_barset(stock[0], 'minute', length)
      self.allStocks[i][1] = (bars[stock[0]][len(bars[stock[0]]) - 1].c - bars[stock[0]][0].o) / bars[stock[0]][0].o

  # Mechanism used to rank the stocks, the basis of the Long-Short Equity Strategy.
  def rank(self):
    # Ranks all stocks by percent change over the past 10 minutes (higher is better).
    tGetPC = threading.Thread(target=self.getPercentChanges)
    tGetPC.start()
    tGetPC.join()

    # Sort the stocks in place by the percent change field (marked by pc).
    self.allStocks.sort(key=lambda x: x[1])

# Run the LongShort class
ls = LongShort()
ls.run()
