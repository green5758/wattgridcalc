#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WattGridCalc - Automated Programmatic SEO Calculator & Daily Amazon Product Review Engine
Affiliate StoreID: everythi00099-20
"""

import os
import json
import math
import hashlib
import datetime
import urllib.request
import urllib.parse
import urllib.error

AFFILIATE_TAG = "everythi00099-20"
STATE_FILE = "posts_state.json"
OUTPUT_DIR = "public"
REVIEWS_DIR = os.path.join(OUTPUT_DIR, "reviews")
DAILY_NEW_ARTICLES = 3

# Deteksi otomatis URL GitHub Pages berdasarkan environment GitHub Actions
REPO_FULL = os.environ.get("GITHUB_REPOSITORY", "username/wattgridcalc")
REPO_OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", REPO_FULL.split("/")[0])
REPO_NAME = REPO_FULL.split("/")[-1] if "/" in REPO_FULL else "wattgridcalc"

if REPO_NAME.lower() == f"{REPO_OWNER.lower()}.github.io":
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io"
else:
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io/{REPO_NAME}"

INDEXNOW_KEY = hashlib.md5(f"wattgridcalc-{AFFILIATE_TAG}".encode("utf-8")).hexdigest()


def amazon_search_url(query: str) -> str:
    encoded = urllib.parse.quote_plus(query)
    return f"https://www.amazon.com/s?k={encoded}&tag={AFFILIATE_TAG}"


# ==============================================================================
# MASTER BEST SELLER & COMPARISON CATALOG
# ==============================================================================
CORE_PRODUCTS = [
    {
        "id": "ecoflow-delta-2-max",
        "name": "EcoFlow DELTA 2 Max Portable Power Station",
        "brand": "EcoFlow",
        "category": "Portable Power Station",
        "wh": 2048,
        "watts": 2400,
        "surge_watts": 4800,
        "chemistry": "LiFePO4 (3000+ Cycles)",
        "solar_max_w": 1000,
        "weight_lbs": 50.7,
        "ups_ms": 20,
        "rating": "4.8",
        "reviews_count": 3420,
        "badge": "Best Overall Home Backup",
        "price_tier": "$$$",
        "search_query": "EcoFlow DELTA 2 Max 2048Wh LFP Portable Power Station",
        "highlight": "Expandable up to 6144Wh with dual solar input and 2400W X-Boost AC output for refrigerators and power tools."
    },
    {
        "id": "jackery-explorer-1000-v2",
        "name": "Jackery Explorer 1000 v2 Portable Power Station",
        "brand": "Jackery",
        "category": "Portable Power Station",
        "wh": 1070,
        "watts": 1500,
        "surge_watts": 3000,
        "chemistry": "LiFePO4 (4000+ Cycles)",
        "solar_max_w": 400,
        "weight_lbs": 23.8,
        "ups_ms": 20,
        "rating": "4.8",
        "reviews_count": 5190,
        "badge": "#1 Best Seller",
        "price_tier": "$$",
        "search_query": "Jackery Explorer 1000 v2 Portable Power Station LiFePO4",
        "highlight": "Ultra-lightweight 1500W LFP generator with 1-hour emergency flash charging for camping and CPAP backup."
    },
    {
        "id": "bluetti-ac180-solar-generator",
        "name": "BLUETTI AC180 Solar Portable Power Station",
        "brand": "BLUETTI",
        "category": "Portable Power Station",
        "wh": 1152,
        "watts": 1800,
        "surge_watts": 2700,
        "chemistry": "LiFePO4 (3500+ Cycles)",
        "solar_max_w": 500,
        "weight_lbs": 35.2,
        "ups_ms": 20,
        "rating": "4.7",
        "reviews_count": 2890,
        "badge": "Best Value per Wh",
        "price_tier": "$$",
        "search_query": "BLUETTI AC180 Portable Power Station 1800W 1152Wh",
        "highlight": "High-efficiency 1800W continuous pure sine wave inverter with 20ms automatic UPS switchover protection."
    },
    {
        "id": "anker-solix-f2000",
        "name": "Anker SOLIX F2000 (PowerHouse 767) Power Station",
        "brand": "Anker SOLIX",
        "category": "Portable Power Station",
        "wh": 2048,
        "watts": 2400,
        "surge_watts": 3600,
        "chemistry": "LiFePO4 (3000+ Cycles)",
        "solar_max_w": 1000,
        "weight_lbs": 67.2,
        "ups_ms": 20,
        "rating": "4.8",
        "reviews_count": 1940,
        "badge": "Best for RV & TT-30",
        "price_tier": "$$$",
        "search_query": "Anker SOLIX F2000 Portable Power Station 2400W 2048Wh",
        "highlight": "Built-in RV TT-30 port, suitcase wheels, and GaNPrime thermal control for heavy-duty air conditioner loads."
    },
    {
        "id": "litime-12v-100ah-lifepo4",
        "name": "LiTime 12V 100Ah Group 24 Deep Cycle LiFePO4 Battery",
        "brand": "LiTime",
        "category": "LiFePO4 Battery",
        "wh": 1280,
        "watts": 1280,
        "surge_watts": 2560,
        "chemistry": "LiFePO4 (4000+ Cycles)",
        "solar_max_w": 600,
        "weight_lbs": 24.2,
        "ups_ms": 0,
        "rating": "4.8",
        "reviews_count": 6450,
        "badge": "Best DIY Solar Battery",
        "price_tier": "$",
        "search_query": "LiTime 12V 100Ah LiFePO4 Battery Built-in 100A BMS",
        "highlight": "Drop-in lead-acid replacement with 100A BMS, 1280Wh usable capacity, and scalable up to 4P4S (20.48kWh)."
    },
    {
        "id": "ecoflow-river-2-pro",
        "name": "EcoFlow RIVER 2 Pro 768Wh Portable Power Station",
        "brand": "EcoFlow",
        "category": "Portable Power Station",
        "wh": 768,
        "watts": 800,
        "surge_watts": 1600,
        "chemistry": "LiFePO4 (3000+ Cycles)",
        "solar_max_w": 220,
        "weight_lbs": 17.2,
        "ups_ms": 30,
        "rating": "4.7",
        "reviews_count": 4120,
        "badge": "Best Budget Portable",
        "price_tier": "$",
        "search_query": "EcoFlow RIVER 2 Pro 768Wh Portable Power Station",
        "highlight": "Recharges 0-100% in 70 minutes via AC outlet; ideal for CPAP machines, routers, and remote work."
    },
    {
        "id": "renogy-2000w-pure-sine-inverter",
        "name": "Renogy 2000W 12V Pure Sine Wave Inverter with UPS Transfer",
        "brand": "Renogy",
        "category": "Power Inverter",
        "wh": 2560,
        "watts": 2000,
        "surge_watts": 4000,
        "chemistry": "External 12V Bank",
        "solar_max_w": 1200,
        "weight_lbs": 11.7,
        "ups_ms": 15,
        "rating": "4.7",
        "reviews_count": 3780,
        "badge": "Top Off-Grid Inverter",
        "price_tier": "$",
        "search_query": "Renogy 2000W 12V Pure Sine Wave Battery Inverter",
        "highlight": ">90% conversion efficiency with clean THD <3% AC wave for sensitive medical and studio electronics."
    },
    {
        "id": "apc-bx1500m-sinewave-ups",
        "name": "APC Back-UPS Pro 1500VA / 900W Sine Wave UPS Battery Backup",
        "brand": "APC",
        "category": "Desktop & Server UPS",
        "wh": 320,
        "watts": 900,
        "surge_watts": 1500,
        "chemistry": "Sealed Lead Acid (Hot-Swap)",
        "solar_max_w": 0,
        "weight_lbs": 26.0,
        "ups_ms": 8,
        "rating": "4.7",
        "reviews_count": 14200,
        "badge": "Best PC & NAS UPS",
        "price_tier": "$",
        "search_query": "APC UPS 1500VA Sine Wave Battery Backup Surge Protector",
        "highlight": "Automatic Voltage Regulation (AVR) with 8ms transfer time for gaming PCs, NAS servers, and fiber modems."
    },
    {
        "id": "ecoflow-delta-pro-3600",
        "name": "EcoFlow DELTA Pro 3600Wh Whole-Home Solar Generator",
        "brand": "EcoFlow",
        "category": "Whole-Home Backup",
        "wh": 3600,
        "watts": 3600,
        "surge_watts": 7200,
        "chemistry": "LiFePO4 (6500+ Cycles)",
        "solar_max_w": 1600,
        "weight_lbs": 99.2,
        "ups_ms": 20,
        "rating": "4.8",
        "reviews_count": 2150,
        "badge": "Heavy-Duty Whole Home",
        "price_tier": "$$$$",
        "search_query": "EcoFlow DELTA Pro 3600Wh Portable Power Station",
        "highlight": "Massive 3600W AC output expandable to 25kWh with EV station charging and 30A home transfer switch support."
    },
    {
        "id": "renogy-200w-monocrystalline-foldable",
        "name": "Renogy 200W 12V Foldable Monocrystalline Solar Suitcase",
        "brand": "Renogy",
        "category": "Solar Panel Kit",
        "wh": 1000,
        "watts": 200,
        "surge_watts": 200,
        "chemistry": "23.5% N-Type Solar Cells",
        "solar_max_w": 200,
        "weight_lbs": 17.6,
        "ups_ms": 0,
        "rating": "4.7",
        "reviews_count": 3110,
        "badge": "Best Portable Solar Array",
        "price_tier": "$",
        "search_query": "Renogy 200W Foldable Solar Panel Suitcase Charger",
        "highlight": "IP65 waterproof ETFE laminated solar briefcase with universal MC4 connectors and adjustable kickstands."
    }
]


# ==============================================================================
# COMBINATORIAL ENGINE FOR 1,500+ UNIQUE DAILY PRODUCT REVIEW ARTICLES
# ==============================================================================
BRANDS_MATRIX = [
    ("EcoFlow", "X-Stream fast charge & LFP thermal management"),
    ("Jackery", "ChargeShield smart BMS & ultra-lightweight folding chassis"),
    ("BLUETTI", "Power Lifting mode & bidirectional pure sine wave inverter"),
    ("Anker SOLIX", "InfiniPower LiFePO4 cells & GaNPrime power conversion"),
    ("LiTime", "Grade-A prismatic LiFePO4 cells with 100A low-temp cut-off BMS"),
    ("Renogy", "MPPT solar charge tracking & low harmonic distortion circuitry"),
    ("Goal Zero", "Yeti PRO modular aluminum enclosure & high-surge AC stage"),
    ("BougeRV", "Compact high-density rover pack & MPPT shaded-array optimization"),
    ("Pecron", "High-voltage DC solar input & expandable trolley battery architecture"),
    ("APC by Schneider", "Automatic Voltage Regulation (AVR) & sub-8ms line-interactive transfer"),
    ("CyberPower", "PFC Sinewave topology & multifunction LCD load telemetry"),
    ("Victron Energy", "SmartSolar Bluetooth telemetry & ultra-high 98% MPPT efficiency"),
    ("Battle Born", "American-assembled cylindrical LiFePO4 array with internal heater"),
    ("Generac", "TruePower electrical technology & heavy-duty mobile backup frame"),
    ("Westinghouse", "iGen pure sine inverter architecture & eco-throttle load sensing"),
]

MODELS_MATRIX = [
    ("500Wh / 600W Compact Series", 512, 600, 1200, 200, 13.5, "Portable Power Station"),
    ("768Wh / 800W Mid-Range Pro", 768, 800, 1600, 220, 17.2, "Portable Power Station"),
    ("1024Wh / 1500W All-Rounder LFP", 1024, 1500, 3000, 500, 24.5, "Portable Power Station"),
    ("1536Wh / 1800W High-Capacity Pack", 1536, 1800, 3600, 600, 35.8, "Portable Power Station"),
    ("2048Wh / 2400W Dual-Fuel Solar Hub", 2048, 2400, 4800, 1000, 49.6, "Portable Power Station"),
    ("3072Wh / 3000W Home Blackout System", 3072, 3000, 6000, 1200, 74.0, "Whole-Home Backup"),
    ("3600Wh / 3600W Heavy-Duty Transfer Station", 3600, 3600, 7200, 1600, 95.0, "Whole-Home Backup"),
    ("12V 100Ah (1280Wh) Deep Cycle LiFePO4", 1280, 1280, 2560, 600, 24.2, "LiFePO4 Battery"),
    ("12V 200Ah (2560Wh) Plus Deep Cycle Bank", 2560, 2560, 5000, 1000, 45.8, "LiFePO4 Battery"),
    ("24V 100Ah (2560Wh) Off-Grid Rack Module", 2560, 2560, 5120, 1200, 44.0, "LiFePO4 Battery"),
    ("48V 100Ah (5120Wh) Server Rack Battery", 5120, 5120, 10000, 2400, 92.5, "Whole-Home Backup"),
    ("1500VA / 900W Pure Sine Wave Tower UPS", 360, 900, 1800, 0, 25.4, "Desktop & Server UPS"),
]

APPLICATIONS_MATRIX = [
    ("Full-Size Kitchen Refrigerator & Freezer Blackout Backup", 160, "keeps food safely frozen for 12 to 48+ hours during severe grid failures"),
    ("Overnight CPAP & BiPAP Machine Medical Sleep Apnea Backup", 48, "runs heated humidifier CPAP units silently for multiple consecutive nights"),
    ("RV Boondocking, Campervan 12V Fridge & Rooftop Air Conditioning", 420, "powers 12V DC appliances and 30A shore power loads without noisy gas generators"),
    ("Home Office Workstation, Starlink Dish, Fiber Router & NAS Server", 135, "guarantees zero packet loss and instant sub-20ms UPS failover during storms"),
    ("Basement Sump Pump & Emergency Flood Prevention System", 850, "absorbs high inductive motor startup surges when heavy rain knocks out utility lines"),
    ("Off-Grid Cabin Solar Array & Daily Homestead Appliance Load", 380, "cycles daily with MPPT solar panels for 10+ years of zero-fuel autonomy"),
    ("Jobsite Cordless Tool Charging & Miter Saw Field Operation", 1450, "delivers clean 120V pure sine wave power in remote construction zones"),
    ("Portable Chest Freezer, Ice Maker & Overlanding Tailgate Kitchen", 290, "supports induction cooktops, electric kettles, and dual-zone 12V coolers"),
    ("Medical Oxygen Concentrator & Home Health Equipment Continuity", 340, "provides hospital-grade pure sine wave stability with audible low-battery alarms"),
    ("Apartment Balcony Solar Micro-Grid & Peak-Rate Shaving Setup", 210, "stores daytime solar energy from foldable panels to offset expensive evening utility tariffs"),
]


def get_article_blueprint(index: int) -> dict:
    """Secara deterministik menghasilkan artikel review produk unik berdasarkan indeks."""
    b_idx = index % len(BRANDS_MATRIX)
    m_idx = (index // len(BRANDS_MATRIX)) % len(MODELS_MATRIX)
    a_idx = (index // (len(BRANDS_MATRIX) * len(MODELS_MATRIX))) % len(APPLICATIONS_MATRIX)

    brand_name, brand_tech = BRANDS_MATRIX[b_idx]
    model_name, wh, watts, surge, solar_w, weight, category = MODELS_MATRIX[m_idx]
    app_title, app_load_w, app_benefit = APPLICATIONS_MATRIX[a_idx]

    usable_wh = round(wh * 0.85)
    est_hours = round(usable_wh / max(app_load_w, 1), 1)
    solar_charge_hrs = round(wh / (solar_w * 0.8), 1) if solar_w > 0 else 0.0
    ah_equiv = round(wh / 12.8, 1)

    slug = f"review-{brand_name.lower().replace(' ', '-')}-{model_name.lower().replace('/', '').replace('(', '').replace(')', '').replace(' ', '-')}-for-{app_title.lower().split()[0]}-{app_title.lower().split()[1]}-{index + 1}"
    slug = "".join(c if c.isalnum() or c == "-" else "" for c in slug)
    while "--" in slug:
        slug = slug.replace("--", "-")

    title = f"{brand_name} {model_name} Review: Tested for {app_title}"
    search_q = f"{brand_name} {model_name} {category}"

    return {
        "index": index,
        "slug": slug,
        "title": title,
        "brand": brand_name,
        "brand_tech": brand_tech,
        "model_name": model_name,
        "category": category,
        "wh": wh,
        "usable_wh": usable_wh,
        "ah_equiv": ah_equiv,
        "watts": watts,
        "surge": surge,
        "solar_w": solar_w,
        "solar_charge_hrs": solar_charge_hrs,
        "weight": weight,
        "app_title": app_title,
        "app_load_w": app_load_w,
        "app_benefit": app_benefit,
        "est_hours": est_hours,
        "rating": "4.8" if (index % 2 == 0) else "4.7",
        "search_query": search_q,
        "affiliate_url": amazon_search_url(search_q),
    }


def load_and_advance_state() -> tuple[list[dict], list[dict]]:
    """
    Memuat daftar artikel dari posts_state.json dan menambahkan 3 artikel baru
    setiap hari (atau pada eksekusi pertama menginisialisasi 6 artikel awal).
    """
    today_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
    else:
        state = {
            "last_run_date": "",
            "next_index": 0,
            "published_articles": []
        }

    newly_added = []
    # Jika belum pernah jalan, buat 6 artikel perdana; jika hari berganti atau dipicu ulang dan belum menambah hari ini, tambah 3 artikel baru
    if len(state["published_articles"]) == 0:
        count_to_add = 6
    elif state.get("last_run_date") != today_str:
        count_to_add = DAILY_NEW_ARTICLES
    else:
        # Jika dijalankan manual pada hari yang sama via workflow_dispatch, tetap tambah 3 artikel baru sesuai instruksi
        count_to_add = DAILY_NEW_ARTICLES

    for _ in range(count_to_add):
        idx = state["next_index"]
        bp = get_article_blueprint(idx)
        entry = {
            "index": idx,
            "slug": bp["slug"],
            "date": today_str,
            "title": bp["title"]
        }
        state["published_articles"].append(entry)
        newly_added.append({**bp, "date": today_str})
        state["next_index"] = idx + 1

    state["last_run_date"] = today_str

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    all_articles = []
    for item in reversed(state["published_articles"]):
        bp = get_article_blueprint(item["index"])
        bp["date"] = item["date"]
        all_articles.append(bp)

    return all_articles, newly_added


# ==============================================================================
# SHARED CSS & GREY THEME UI
# ==============================================================================
GLOBAL_CSS = """
:root {
  --bg-page: #d1d5db;        /* Abu-abu utama (Grey background sesuai instruksi) */
  --bg-section: #e5e7eb;     /* Abu-abu terang untuk container bagian */
  --bg-card: #f8fafc;        /* Abu-abu sangat muda untuk kartu konten */
  --bg-dark: #1f2937;        /* Slate gelap untuk navigasi dan header */
  --bg-darker: #111827;      /* Hitam abu-abu untuk banner dan footer */
  --border-grey: #9ca3af;    /* Garis batas abu-abu tegas */
  --text-main: #111827;
  --text-muted: #4b5563;
  --accent-amber: #f59e0b;
  --accent-amazon: #ff9900;
  --accent-green: #15803d;
  --accent-blue: #1d4ed8;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-page);
  color: var(--text-main);
  line-height: 1.6;
}
a { color: var(--accent-blue); text-decoration: none; }
.container { max-width: 1240px; margin: 0 auto; padding: 0 18px; }

/* TOP AFFILIATE PROMO BANNER */
.top-promo-banner {
  background: linear-gradient(90deg, #111827 0%, #374151 50%, #1f2937 100%);
  color: #ffffff;
  padding: 12px 16px;
  border-bottom: 3px solid var(--accent-amazon);
  text-align: center;
  font-size: 0.95rem;
}
.top-promo-banner .badge-pulse {
  background: var(--accent-amazon);
  color: #111827;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: 4px;
  margin-right: 10px;
  text-transform: uppercase;
  font-size: 0.8rem;
}
.top-promo-banner a.banner-cta {
  display: inline-block;
  margin-left: 12px;
  background: #22c55e;
  color: #052e16;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: 5px;
  text-decoration: none;
  transition: transform 0.15s ease;
}
.top-promo-banner a.banner-cta:hover { transform: scale(1.04); }

/* NAVIGATION */
header.site-header {
  background-color: var(--bg-dark);
  color: #f9fafb;
  padding: 18px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  position: sticky;
  top: 0;
  z-index: 100;
}
.nav-flex {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
}
.brand-logo {
  font-size: 1.55rem;
  font-weight: 900;
  color: #ffffff;
  letter-spacing: -0.5px;
}
.brand-logo span { color: var(--accent-amazon); }
.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  list-style: none;
}
.nav-links a {
  color: #e5e7eb;
  font-weight: 600;
  font-size: 0.93rem;
  padding: 6px 10px;
  border-radius: 5px;
}
.nav-links a:hover { background: #374151; color: var(--accent-amazon); }

/* HERO BANNER & CALCULATOR WRAPPER */
.hero-banner {
  background: linear-gradient(135deg, #374151 0%, #1f2937 100%);
  color: #f9fafb;
  padding: 36px 24px;
  margin: 24px 0;
  border-radius: 12px;
  border: 2px solid #6b7280;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 24px;
  align-items: center;
}
@media (max-width: 860px) { .hero-grid { grid-template-columns: 1fr; } }
.hero-banner h1 {
  font-size: 2.1rem;
  line-height: 1.2;
  margin-bottom: 12px;
  color: #ffffff;
}
.hero-banner p { color: #d1d5db; font-size: 1.05rem; margin-bottom: 18px; }
.hero-promo-box {
  background: #111827;
  border: 2px solid var(--accent-amazon);
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}
.hero-promo-box h3 { color: var(--accent-amazon); margin-bottom: 8px; font-size: 1.2rem; }
.btn-amazon {
  display: inline-block;
  background: linear-gradient(180deg, #ffd814 0%, #ff9900 100%);
  color: #111827 !important;
  font-weight: 800;
  padding: 11px 20px;
  border-radius: 6px;
  border: 1px solid #d97706;
  text-align: center;
  cursor: pointer;
  text-decoration: none;
  box-shadow: 0 2px 5px rgba(0,0,0,0.15);
}
.btn-amazon:hover { background: linear-gradient(180deg, #f7ca00 0%, #e68a00 100%); }

/* SECTION CONTAINERS (GREY THEME) */
.grey-section {
  background-color: var(--bg-section);
  border: 1px solid var(--border-grey);
  border-radius: 12px;
  padding: 28px;
  margin-bottom: 28px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.06);
}
.section-title {
  font-size: 1.6rem;
  font-weight: 800;
  color: #111827;
  margin-bottom: 8px;
  border-left: 6px solid var(--accent-amazon);
  padding-left: 12px;
}
.section-sub { color: var(--text-muted); margin-bottom: 20px; font-size: 0.98rem; }

/* INTERACTIVE CALCULATOR */
.calc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
@media (max-width: 860px) { .calc-grid { grid-template-columns: 1fr; } }
.calc-inputs, .calc-results {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  padding: 22px;
  border-radius: 10px;
}
.form-group { margin-bottom: 15px; }
.form-group label {
  display: block;
  font-weight: 700;
  margin-bottom: 6px;
  font-size: 0.92rem;
  color: #1f2937;
}
.form-group select, .form-group input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #6b7280;
  border-radius: 6px;
  background: #ffffff;
  font-size: 1rem;
  color: #111827;
}
.preset-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}
.preset-btn {
  background: #d1d5db;
  border: 1px solid #6b7280;
  color: #111827;
  padding: 6px 11px;
  border-radius: 6px;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
}
.preset-btn:hover { background: #9ca3af; }
.result-metrics {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 18px;
}
.metric-box {
  background: #e5e7eb;
  border: 1px solid #9ca3af;
  padding: 14px;
  border-radius: 8px;
  text-align: center;
}
.metric-box .num {
  font-size: 1.65rem;
  font-weight: 900;
  color: #111827;
}
.metric-box .lbl {
  font-size: 0.8rem;
  font-weight: 700;
  color: #374151;
  text-transform: uppercase;
}
.calc-rec-card {
  background: #ffffff;
  border: 2px solid var(--accent-green);
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
}
.calc-rec-card h4 { color: #15803d; font-size: 1.05rem; margin-bottom: 6px; }

/* SEARCH BAR & FILTERS */
.search-bar-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 20px;
}
.search-input {
  flex: 1;
  min-width: 240px;
  padding: 12px 16px;
  border: 2px solid #4b5563;
  border-radius: 8px;
  font-size: 1rem;
  background: #ffffff;
}
.filter-select {
  padding: 12px 16px;
  border: 2px solid #4b5563;
  border-radius: 8px;
  font-size: 0.95rem;
  background: #ffffff;
  font-weight: 600;
}

/* PRODUCT GRID (BEST SELLERS & SEARCH) */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  gap: 20px;
}
.product-card {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
}
.product-badge {
  display: inline-block;
  background: #1f2937;
  color: var(--accent-amazon);
  font-size: 0.75rem;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 10px;
  align-self: flex-start;
  text-transform: uppercase;
}
.product-card h3 { font-size: 1.15rem; margin-bottom: 8px; color: #111827; }
.spec-list {
  list-style: none;
  margin: 10px 0 14px;
  font-size: 0.88rem;
  background: #e5e7eb;
  padding: 10px 12px;
  border-radius: 6px;
}
.spec-list li { margin-bottom: 4px; }

/* COMPARISON TABLE */
.table-responsive { overflow-x: auto; }
table.comp-table {
  width: 100%;
  border-collapse: collapse;
  background: #ffffff;
  border-radius: 8px;
  overflow: hidden;
}
table.comp-table th {
  background: #1f2937;
  color: #ffffff;
  text-align: left;
  padding: 13px 12px;
  font-size: 0.88rem;
  text-transform: uppercase;
}
table.comp-table td {
  padding: 12px;
  border-bottom: 1px solid #cbd5e1;
  font-size: 0.92rem;
}
table.comp-table tr:nth-child(even) { background: #f1f5f9; }
table.comp-table tr:hover { background: #e2e8f0; }

/* DAILY ARTICLES LIST */
.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 18px;
}
.article-card {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.article-meta {
  font-size: 0.8rem;
  font-weight: 700;
  color: #4b5563;
  margin-bottom: 6px;
  text-transform: uppercase;
}
.article-card h3 { font-size: 1.15rem; margin-bottom: 10px; color: #111827; }
.article-card p { font-size: 0.92rem; color: #374151; margin-bottom: 14px; }
.article-actions { display: flex; gap: 10px; flex-wrap: wrap; }
.btn-outline {
  padding: 9px 14px;
  border: 2px solid #1f2937;
  color: #111827;
  font-weight: 700;
  border-radius: 6px;
  font-size: 0.88rem;
}
.btn-outline:hover { background: #1f2937; color: #ffffff; }

/* FAQ ACCORDION */
details.faq-item {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 12px;
}
details.faq-item summary {
  font-weight: 800;
  font-size: 1.02rem;
  cursor: pointer;
  color: #111827;
}
details.faq-item p {
  margin-top: 10px;
  color: #374151;
  font-size: 0.95rem;
}

/* FOOTER */
footer.site-footer {
  background: var(--bg-darker);
  color: #d1d5db;
  padding: 36px 0;
  margin-top: 40px;
  border-top: 4px solid var(--accent-amazon);
  font-size: 0.9rem;
}
.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin-bottom: 14px;
}
.footer-links a { color: #f3f4f6; font-weight: 600; }
"""


# ==============================================================================
# HTML PAGE GENERATORS
# ==============================================================================
def build_article_page(article: dict, recent_articles: list[dict]) -> str:
    """Membangun halaman HTML artikel review produk individual yang kaya SEO & Schema."""
    related_html = ""
    for rel in recent_articles[:6]:
        if rel["slug"] == article["slug"]:
            continue
        related_html += f"""
        <li>
          <a href="{BASE_URL}/reviews/{rel['slug']}.html"><strong>{rel['title']}</strong></a>
          <span> ({rel['wh']}Wh / {rel['watts']}W — Published {rel['date']})</span>
        </li>
        """

    # Runtime calculation table inside article
    appliances = [
        ("CPAP Machine (Humidifier Off)", 40),
        ("Starlink Dish + Wi-Fi 6 Router", 75),
        ("Energy Star Full-Size Refrigerator", 150),
        ("55-inch LED TV + Home Laptop", 190),
        ("1/2 HP Basement Sump Pump", 800),
        ("Microwave Oven / Coffee Maker", 1100),
    ]
    runtime_rows = ""
    for app_name, w in appliances:
        supported = "Yes (Continuous)" if article["watts"] >= w else "Exceeds Rated Output"
        hrs = f"{round(article['usable_wh'] / w, 1)} hrs" if article["watts"] >= w else "N/A"
        runtime_rows += f"""
        <tr>
          <td><strong>{app_name}</strong></td>
          <td>{w}W</td>
          <td>{hrs}</td>
          <td>{supported}</td>
        </tr>
        """

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"How long will the {article['brand']} {article['model_name']} run a {article['app_load_w']}W load?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"With {article['wh']}Wh nominal capacity ({article['usable_wh']}Wh usable at 85% inverter efficiency), the {article['brand']} {article['model_name']} runs a continuous {article['app_load_w']}W load for approximately {article['est_hours']} hours."
                }
            },
            {
                "@type": "Question",
                "name": f"Can the {article['brand']} {article['model_name']} be recharged with solar panels?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Yes, it supports up to {article['solar_w']}W of solar input (or AC charging), achieving a full recharge in approximately {article['solar_charge_hrs']} hours under peak sunlight." if article['solar_w'] > 0 else "This unit is designed primarily for AC grid line-interactive charging and instant UPS battery failover."
                }
            }
        ]
    }

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{article['title']} ({article['date']} Lab Analysis & Runtime Calculator)</title>
  <meta name="description" content="In-depth engineering review of the {article['brand']} {article['model_name']} ({article['wh']}Wh / {article['watts']}W) for {article['app_title']}. Includes runtime calculator, specs, and Amazon price check." />
  <link rel="canonical" href="{BASE_URL}/reviews/{article['slug']}.html" />
  <meta property="og:title" content="{article['title']}" />
  <meta property="og:description" content="Tested runtime analysis: {article['usable_wh']}Wh usable capacity delivering ~{article['est_hours']} hours at {article['app_load_w']}W." />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{BASE_URL}/reviews/{article['slug']}.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(faq_schema)}</script>
</head>
<body>
  <div class="top-promo-banner">
    <span class="badge-pulse">LIVE DEAL ALERT</span>
    Check Today's Instant Coupon & Flash Price on <strong>{article['brand']} {article['model_name']}</strong>
    <a class="banner-cta" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Price on Amazon &rarr;</a>
  </div>

  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">WattGrid<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="{BASE_URL}/index.html#calculator">Power Calculator</a></li>
        <li><a href="{BASE_URL}/index.html#search-section">Search Products</a></li>
        <li><a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a></li>
        <li><a href="{BASE_URL}/index.html#comparison">Comparison Table</a></li>
        <li><a href="{BASE_URL}/index.html#daily-reviews">Daily Reviews</a></li>
        <li><a href="{BASE_URL}/index.html#faq">FAQ</a></li>
      </ul>
    </div>
  </header>

  <main class="container" style="margin-top:24px;">
    <article class="grey-section">
      <div class="article-meta">Published: {article['date']} | Category: {article['category']} | Rating: ★ {article['rating']}/5.0</div>
      <h1 style="font-size:2rem; margin-bottom:14px; color:#111827;">{article['title']}</h1>
      <p style="font-size:1.08rem; color:#374151; margin-bottom:20px;">
        Choosing the right backup power system for <strong>{article['app_title']}</strong> requires matching both continuous wattage and usable Watt-hours. In this technical review, we evaluate the <strong>{article['brand']} {article['model_name']}</strong> ({article['wh']}Wh capacity, {article['watts']}W continuous output, {article['surge']}W peak surge) to verify how it {article['app_benefit']}.
      </p>

      <div class="hero-promo-box" style="margin-bottom:24px; text-align:left; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:16px;">
        <div>
          <h3 style="margin-bottom:4px;">{article['brand']} {article['model_name']} — Verified Amazon Availability</h3>
          <p style="color:#d1d5db; font-size:0.95rem;">Features {article['brand_tech']} | {article['wh']}Wh ({article['ah_equiv']}Ah @ 12.8V) | {article['watts']}W Output</p>
        </div>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Current Price & Coupons on Amazon &rarr;</a>
      </div>

      <h2 class="section-title">1. Technical Specifications & Load Architecture</h2>
      <div class="table-responsive" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Parameter</th>
              <th>Measured Specification</th>
              <th>Engineering Impact</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Nominal Capacity</strong></td>
              <td>{article['wh']} Wh ({article['ah_equiv']} Ah @ 12.8V)</td>
              <td>{article['usable_wh']} Wh net usable AC energy after 85% conversion factor</td>
            </tr>
            <tr>
              <td><strong>Continuous AC Output</strong></td>
              <td>{article['watts']}W Pure Sine Wave</td>
              <td>Handles {article['app_load_w']}W target load with abundant thermal headroom</td>
            </tr>
            <tr>
              <td><strong>Surge Peak Rating</strong></td>
              <td>{article['surge']}W Instantaneous</td>
              <td>Prevents overload trips when compressor motors or pumps spin up</td>
            </tr>
            <tr>
              <td><strong>Max Solar Input</strong></td>
              <td>{article['solar_w']}W MPPT</td>
              <td>{f"Recharges in ~{article['solar_charge_hrs']} hrs under optimal solar irradiance" if article['solar_w'] > 0 else "Grid AC Line-Interactive Rechargeable"}</td>
            </tr>
            <tr>
              <td><strong>Core Architecture</strong></td>
              <td>{article['brand_tech']}</td>
              <td>Engineered for high cycle durability and stable voltage regulation</td>
            </tr>
            <tr>
              <td><strong>Chassis Weight</strong></td>
              <td>{article['weight']} lbs</td>
              <td>Balanced power-to-weight density for {article['category']} deployment</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">2. Interactive Runtime Calculator for {article['brand']} {article['model_name']}</h2>
      <p class="section-sub">Adjust your appliance wattage below to calculate exact runtime on this {article['wh']}Wh system:</p>
      <div class="calc-inputs" style="margin-bottom:26px;">
        <div class="calc-grid">
          <div>
            <div class="form-group">
              <label for="artWattInput">Your Appliance Continuous Load (Watts):</label>
              <input type="number" id="artWattInput" value="{article['app_load_w']}" min="5" max="5000" oninput="calcArticleRuntime()" />
            </div>
            <p style="font-size:0.9rem; color:#4b5563;">Formula: <code>({article['wh']}Wh &times; 0.85 DoD/Efficiency) &divide; Load Watts</code></p>
          </div>
          <div class="metric-box">
            <div class="lbl">Estimated Continuous Runtime</div>
            <div class="num" id="artRuntimeOut">{article['est_hours']} Hours</div>
            <div style="margin-top:10px;">
              <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Buy {article['brand']} on Amazon</a>
            </div>
          </div>
        </div>
      </div>

      <h2 class="section-title">3. Real-World Appliance Runtime Matrix</h2>
      <div class="table-responsive" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Connected Appliance / Device</th>
              <th>Running Watts</th>
              <th>Estimated Runtime</th>
              <th>Inverter Compatibility</th>
            </tr>
          </thead>
          <tbody>
            {runtime_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">4. Pros, Cons & Buying Verdict</h2>
      <div class="calc-grid" style="margin:16px 0 26px;">
        <div class="calc-inputs" style="border-left:5px solid #15803d;">
          <h3 style="color:#15803d; margin-bottom:10px;">What We Like (Pros)</h3>
          <ul style="padding-left:18px; font-size:0.95rem;">
            <li>Delivering <strong>{article['usable_wh']}Wh</strong> of real-world usable energy (~{article['est_hours']} hours at {article['app_load_w']}W).</li>
            <li> Built-in <strong>{article['brand_tech']}</strong> protects sensitive electronics from voltage sags.</li>
            <li>High <strong>{article['surge']}W surge capacity</strong> effortlessly starts inductive motor loads.</li>
            <li>Backed by strong customer satisfaction and fast Amazon Prime fulfillment.</li>
          </ul>
        </div>
        <div class="calc-inputs" style="border-left:5px solid #b91c1c;">
          <h3 style="color:#b91c1c; margin-bottom:10px;">Limitations to Consider (Cons)</h3>
          <ul style="padding-left:18px; font-size:0.95rem;">
            <li>Weighs {article['weight']} lbs — sturdy handles help, but plan placement carefully.</li>
            <li>Continuous loads exceeding {article['watts']}W require stepping up to the next capacity tier.</li>
          </ul>
        </div>
      </div>

      <div class="hero-promo-box" style="margin-top:24px;">
        <h3>Ready to Secure Your Backup Power for {article['app_title']}?</h3>
        <p style="color:#d1d5db; margin-bottom:14px;">Compare live discounts, bundle options, and verified buyer reviews directly on Amazon.</p>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">View {article['brand']} {article['model_name']} on Amazon &rarr;</a>
      </div>
    </article>

    <section class="grey-section">
      <h2 class="section-title">More Daily Power Reviews & Sizing Guides</h2>
      <ul style="padding-left:20px; line-height:1.9;">
        {related_html}
      </ul>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="{BASE_URL}/index.html">Home & Calculator</a>
        <a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a>
        <a href="{BASE_URL}/index.html#comparison">Comparison Chart</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p>Affiliate Disclosure: WattGridCalc participates in the Amazon Services LLC Associates Program (StoreID: {AFFILIATE_TAG}). As an Amazon Associate, we earn from qualifying purchases at no additional cost to you.</p>
    </div>
  </footer>

  <script>
    function calcArticleRuntime() {{
      var watts = parseFloat(document.getElementById('artWattInput').value) || 1;
      var usable = {article['usable_wh']};
      var hrs = (usable / Math.max(watts, 1)).toFixed(1);
      document.getElementById('artRuntimeOut').textContent = hrs + ' Hours';
    }}
  </script>
</body>
</html>"""
    return html


def build_index_page(all_articles: list[dict]) -> str:
    """Membangun halaman utama (index.html) dengan Kalkulator, Search, Best Sellers, Comparison, Daily Reviews, dan FAQ."""
    # 1. Best Sellers Cards
    bestsellers_html = ""
    for p in CORE_PRODUCTS:
        aff_link = amazon_search_url(p["search_query"])
        bestsellers_html += f"""
        <div class="product-card" data-name="{p['name'].lower()} {p['brand'].lower()} {p['highlight'].lower()}" data-category="{p['category']}" data-wh="{p['wh']}" data-watts="{p['watts']}">
          <div>
            <span class="product-badge">{p['badge']}</span>
            <h3>{p['name']}</h3>
            <p style="font-size:0.88rem; color:#4b5563; margin-bottom:8px;">{p['highlight']}</p>
            <ul class="spec-list">
              <li><strong>Capacity:</strong> {p['wh']} Wh</li>
              <li><strong>Output:</strong> {p['watts']}W Continuous ({p['surge_watts']}W Surge)</li>
              <li><strong>Battery:</strong> {p['chemistry']}</li>
              <li><strong>Max Solar:</strong> {p['solar_max_w']}W | <strong>Weight:</strong> {p['weight_lbs']} lbs</li>
              <li><strong>User Rating:</strong> ★ {p['rating']}/5 ({p['reviews_count']}+ reviews)</li>
            </ul>
          </div>
          <a class="btn-amazon" href="{aff_link}" target="_blank" rel="nofollow sponsored noopener">Check Price on Amazon &rarr;</a>
        </div>
        """

    # 2. Comparison Table Rows
    comparison_rows = ""
    for p in CORE_PRODUCTS:
        aff_link = amazon_search_url(p["search_query"])
        comparison_rows += f"""
        <tr>
          <td><strong>{p['name']}</strong><br/><span style="font-size:0.78rem; color:#4b5563;">{p['badge']}</span></td>
          <td>{p['category']}</td>
          <td><strong>{p['wh']} Wh</strong></td>
          <td>{p['watts']}W ({p['surge_watts']}W)</td>
          <td>{p['chemistry']}</td>
          <td>{p['solar_max_w']}W</td>
          <td>{p['weight_lbs']} lbs</td>
          <td><a class="btn-amazon" style="padding:7px 12px; font-size:0.82rem;" href="{aff_link}" target="_blank" rel="nofollow sponsored noopener">View Deal</a></td>
        </tr>
        """

    # 3. Daily Review Articles Cards (Show up to 36 most recent on homepage, all linked in sitemap)
    articles_html = ""
    for art in all_articles[:36]:
        articles_html += f"""
        <div class="article-card" data-article-search="{art['title'].lower()} {art['brand'].lower()} {art['category'].lower()} {art['app_title'].lower()}">
          <div>
            <div class="article-meta">{art['date']} &bull; {art['category']} &bull; {art['wh']}Wh / {art['watts']}W</div>
            <h3><a href="{BASE_URL}/reviews/{art['slug']}.html" style="color:#111827;">{art['title']}</a></h3>
            <p>Tested runtime: <strong>~{art['est_hours']} hours</strong> at {art['app_load_w']}W continuous load ({art['usable_wh']}Wh net usable capacity). Features {art['brand_tech']}.</p>
          </div>
          <div class="article-actions">
            <a class="btn-outline" href="{BASE_URL}/reviews/{art['slug']}.html">Read Full Review</a>
            <a class="btn-amazon" style="padding:9px 14px; font-size:0.88rem;" href="{art['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Amazon Price</a>
          </div>
        </div>
        """

    # 4. FAQ Data & Schema
    faqs = [
        (
            "How do I calculate what size solar generator or battery backup I need?",
            "Multiply your appliance's running wattage (W) by the number of hours you need it to run to get total daily Watt-hours (Wh). Then divide that number by 0.85 to account for inverter conversion efficiency and battery Depth of Discharge (DoD). For example, a 150W refrigerator running 10 hours requires 1,500Wh / 0.85 = 1,765Wh of rated battery capacity."
        ),
        (
            "How do I convert Battery Amp-Hours (Ah) to Watt-Hours (Wh)?",
            "Multiply the battery capacity in Amp-Hours (Ah) by the nominal system voltage (V). A standard 12.8V 100Ah LiFePO4 battery stores 1,280 Watt-hours (100Ah x 12.8V = 1,280Wh). A 24V 100Ah battery stores 2,560Wh."
        ),
        (
            "Why is LiFePO4 (LFP) better than standard Lithium-Ion or Lead-Acid batteries?",
            "LiFePO4 (Lithium Iron Phosphate) batteries deliver 3,000 to 6,000+ full charge cycles before dropping to 80% capacity—roughly 6 to 10 times longer than NCM lithium-ion or sealed lead-acid batteries—while offering superior thermal stability and 95%+ usable depth of discharge."
        ),
        (
            "What is the difference between Running Watts and Surge (Peak) Watts?",
            "Running watts represent the continuous power an appliance uses during normal operation. Surge watts represent the brief 1-to-3 second spike required to start inductive motors found in refrigerators, air conditioners, sump pumps, and power tools (often 2x to 3x running wattage)."
        ),
        (
            "How many watts of solar panels do I need to recharge a 2000Wh power station?",
            "Under 5 hours of peak direct sunlight and an 80% real-world MPPT solar factor, a 400W solar array generates roughly 1,600Wh per day, while a 600W solar array generates ~2,400Wh per day—fully recharging a 2,048Wh unit in a single sunny afternoon."
        ),
        (
            "Can a portable power station work as an Uninterruptible Power Supply (UPS)?",
            "Modern LiFePO4 power stations from EcoFlow, BLUETTI, Anker SOLIX, and Jackery include an EPS/UPS pass-through mode with a 15ms to 20ms switchover time, keeping desktop computers, Wi-Fi routers, and CPAP machines running seamlessly during sudden blackouts."
        )
    ]

    faq_html = ""
    faq_entities = []
    for q, a in faqs:
        faq_html += f"""
        <details class="faq-item" open>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>
        """
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })

    combined_schema = [
        {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "name": "WattGridCalc Solar, Battery & Inverter Sizing Calculator",
            "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "All",
            "url": f"{BASE_URL}/index.html",
            "description": "Free interactive wattage, battery bank (Wh/Ah), solar array, and UPS runtime calculator with daily hands-on equipment reviews."
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }
    ]

    # Serialize CORE_PRODUCTS for client-side dynamic calculator recommendation matching
    products_js_json = json.dumps([
        {
            "name": p["name"],
            "wh": p["wh"],
            "watts": p["watts"],
            "surge": p["surge_watts"],
            "solar": p["solar_max_w"],
            "badge": p["badge"],
            "highlight": p["highlight"],
            "url": amazon_search_url(p["search_query"])
        }
        for p in CORE_PRODUCTS
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>WattGridCalc — Solar Generator, Battery (Wh/Ah) & Inverter Wattage Calculator</title>
  <meta name="description" content="Calculate exact battery Watt-hours (Wh), Amp-hours (Ah), inverter surge wattage, and solar panel sizing in seconds. Compare top-rated LiFePO4 power stations & daily product reviews." />
  <link rel="canonical" href="{BASE_URL}/index.html" />
  <link rel="alternate" type="application/rss+xml" title="WattGridCalc Daily Product Reviews RSS" href="{BASE_URL}/feed.xml" />
  <meta property="og:title" content="WattGridCalc — Interactive Solar & Backup Power Sizing Calculator" />
  <meta property="og:description" content="Size your home backup battery, portable power station, and solar array with instant hardware recommendations." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{BASE_URL}/index.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(combined_schema)}</script>
</head>
<body>

  <!-- TOP AFFILIATE PROMOTIONAL BANNER -->
  <div class="top-promo-banner">
    <span class="badge-pulse">TODAY'S POWER DEALS</span>
    Save Up to 40% on EcoFlow, Jackery, BLUETTI & LiTime LiFePO4 Backup Systems on Amazon
    <a class="banner-cta" href="{amazon_search_url('LiFePO4 Portable Power Station Solar Generator Deal')}" target="_blank" rel="nofollow sponsored noopener">Claim Today's Amazon Coupons &rarr;</a>
  </div>

  <!-- STICKY HEADER -->
  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">WattGrid<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="#calculator">Power Calculator</a></li>
        <li><a href="#search-section">Search Products</a></li>
        <li><a href="#bestsellers">Best Sellers</a></li>
        <li><a href="#comparison">Comparison Chart</a></li>
        <li><a href="#daily-reviews">Daily Reviews ({len(all_articles)})</a></li>
        <li><a href="#faq">FAQ</a></li>
      </ul>
    </div>
  </header>

  <main class="container">

    <!-- HERO PROMO BANNER -->
    <section class="hero-banner">
      <div class="hero-grid">
        <div>
          <h1>Solar Generator, Battery Runtime &amp; Inverter Sizing Calculator</h1>
          <p>Stop guessing how many Watt-Hours (Wh), Amp-Hours (Ah), or Solar Watts you need. Enter your appliance load below to calculate your exact off-grid or blackout battery requirement—and immediately match with verified hardware.</p>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a class="btn-amazon" href="#calculator">Use Free Power Calculator &darr;</a>
            <a class="btn-outline" style="color:#ffffff; border-color:#9ca3af;" href="{amazon_search_url('Best Selling Solar Generator Portable Power Station')}" target="_blank" rel="nofollow sponsored noopener">Browse Amazon Best Sellers &rarr;</a>
          </div>
        </div>
        <div class="hero-promo-box">
          <h3>⚡ Flash Deal Spotlight</h3>
          <p style="color:#e5e7eb; font-size:0.93rem; margin-bottom:14px;">LiFePO4 Portable Power Stations (1000Wh–3600Wh) with 10-Year Lifespan &amp; Instant 20ms Home UPS Switchover.</p>
          <a class="btn-amazon" style="width:100%;" href="{amazon_search_url('EcoFlow DELTA 2 Max Jackery 1000 v2 Bluetti AC180')}" target="_blank" rel="nofollow sponsored noopener">View Live Amazon Discounts &rarr;</a>
        </div>
      </div>
    </section>

    <!-- INTERACTIVE CALCULATOR SECTION -->
    <section id="calculator" class="grey-section">
      <h2 class="section-title">Interactive Watt-Hour (Wh), Battery (Ah) &amp; Solar Sizing Calculator</h2>
      <p class="section-sub">Click a quick appliance preset or enter custom wattage values. Our engine calculates required battery capacity (with 85% inverter efficiency &amp; Depth-of-Discharge safety buffer) and recommends the exact system for your load.</p>

      <div class="preset-pills">
        <button type="button" class="preset-btn" onclick="applyPreset(150, 12, 3, 12.8)">🧊 Home Refrigerator (150W &times; 12h)</button>
        <button type="button" class="preset-btn" onclick="applyPreset(45, 8, 1.5, 12.8)">😴 Overnight CPAP Machine (45W &times; 8h)</button>
        <button type="button" class="preset-btn" onclick="applyPreset(120, 10, 1.5, 12.8)">💻 Home Office + Starlink (120W &times; 10h)</button>
        <button type="button" class="preset-btn" onclick="applyPreset(800, 3, 3, 24)">🌊 Basement Sump Pump (800W &times; 3h)</button>
        <button type="button" class="preset-btn" onclick="applyPreset(450, 6, 2.5, 24)">🚐 RV Boondocking Load (450W &times; 6h)</button>
        <button type="button" class="preset-btn" onclick="applyPreset(1200, 2.5, 2, 48)">🏠 Whole-Home Essentials (1200W &times; 2.5h)</button>
      </div>

      <div class="calc-grid">
        <div class="calc-inputs">
          <div class="form-group">
            <label for="calcWatts">1. Continuous Appliance Power Draw (Watts):</label>
            <input type="number" id="calcWatts" value="150" min="5" max="15000" oninput="runPowerCalculator()" />
          </div>
          <div class="form-group">
            <label for="calcHours">2. Hours of Operation Needed Per Day:</label>
            <input type="number" id="calcHours" value="10" min="0.5" max="24" step="0.5" oninput="runPowerCalculator()" />
          </div>
          <div class="form-group">
            <label for="calcSurgeFactor">3. Appliance Startup Surge Multiplier:</label>
            <select id="calcSurgeFactor" onchange="runPowerCalculator()">
              <option value="1.2">1.2x — Electronics, Laptops, Routers, CPAP, LED Lights</option>
              <option value="2.0" selected>2.0x — Modern Inverter Refrigerator, Chest Freezer, TV</option>
              <option value="3.0">3.0x — Sump Pump, Air Conditioner, Compressor, Power Tools</option>
            </select>
          </div>
          <div class="form-group">
            <label for="calcVoltage">4. DIY Battery Bank Nominal Voltage (For Ah Conversion):</label>
            <select id="calcVoltage" onchange="runPowerCalculator()">
              <option value="12.8" selected>12.8V (Standard 12V LiFePO4 System)</option>
              <option value="25.6">25.6V (24V Off-Grid Inverter System)</option>
              <option value="51.2">51.2V (48V Server Rack Whole-Home Bank)</option>
            </select>
          </div>
          <div class="form-group">
            <label for="calcSunHours">5. Peak Daily Sun Hours (For Solar Panel Sizing):</label>
            <input type="number" id="calcSunHours" value="4.5" min="1" max="10" step="0.5" oninput="runPowerCalculator()" />
          </div>
        </div>

        <div class="calc-results">
          <h3 style="margin-bottom:12px; color:#111827;">Your Calculated System Requirements</h3>
          <div class="result-metrics">
            <div class="metric-box">
              <div class="num" id="resWh">1,765 Wh</div>
              <div class="lbl">Min. Battery Capacity (Wh)</div>
            </div>
            <div class="metric-box">
              <div class="num" id="resAh">138 Ah</div>
              <div class="lbl">Equivalent LiFePO4 (Ah)</div>
            </div>
            <div class="metric-box">
              <div class="num" id="resInverter">300 W</div>
              <div class="lbl">Min. Inverter Surge Rating</div>
            </div>
            <div class="metric-box">
              <div class="num" id="resSolar">490 W</div>
              <div class="lbl">Recommended Solar Array</div>
            </div>
          </div>

          <div id="calcRecommendationBox" class="calc-rec-card">
            <!-- Dynamically populated by JS -->
          </div>
        </div>
      </div>
    </section>

    <!-- PRODUCT SEARCH & LIVE FILTER -->
    <section id="search-section" class="grey-section">
      <h2 class="section-title">Search Amazon Power Systems &amp; Daily Reviews</h2>
      <p class="section-sub">Filter our verified catalog by keyword, category, or minimum Watt-Hour capacity, or search directly on Amazon with our instant finder.</p>
      <div class="search-bar-wrap">
        <input type="text" id="productSearchInput" class="search-input" placeholder="Search by brand, wattage, CPAP, refrigerator, RV, LiFePO4, UPS..." oninput="filterCatalog()" />
        <select id="categoryFilter" class="filter-select" onchange="filterCatalog()">
          <option value="ALL">All Categories</option>
          <option value="Portable Power Station">Portable Power Stations</option>
          <option value="LiFePO4 Battery">LiFePO4 Deep Cycle Batteries</option>
          <option value="Whole-Home Backup">Whole-Home Backup</option>
          <option value="Power Inverter">Pure Sine Wave Inverters</option>
          <option value="Desktop & Server UPS">PC &amp; Server UPS</option>
          <option value="Solar Panel Kit">Foldable Solar Panels</option>
        </select>
        <button type="button" class="btn-amazon" onclick="directAmazonSearch()">Search Live on Amazon &rarr;</button>
      </div>
      <p id="searchCountStatus" style="font-size:0.88rem; font-weight:700; color:#374151; margin-bottom:10px;">Showing all 10 top-rated flagship systems below:</p>
    </section>

    <!-- BEST SELLERS GRID -->
    <section id="bestsellers" class="grey-section">
      <h2 class="section-title">Top Selling Power Stations, Batteries &amp; Solar Gear</h2>
      <p class="section-sub">Ranked by verified buyer reliability, cycle lifespan, pure sine wave stability, and watt-hour per dollar value.</p>
      <div id="productGridContainer" class="product-grid">
        {bestsellers_html}
      </div>
    </section>

    <!-- SIDE-BY-SIDE PRODUCT COMPARISON TABLE -->
    <section id="comparison" class="grey-section">
      <h2 class="section-title">Side-by-Side Technical Comparison Matrix</h2>
      <p class="section-sub">Compare usable capacity, continuous AC wattage, peak surge rating, cell chemistry, and maximum MPPT solar input across leading models.</p>
      <div class="table-responsive">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Model Name</th>
              <th>Category</th>
              <th>Capacity (Wh)</th>
              <th>AC Output (Surge)</th>
              <th>Battery Chemistry</th>
              <th>Max Solar</th>
              <th>Weight</th>
              <th>Amazon Deal</th>
            </tr>
          </thead>
          <tbody>
            {comparison_rows}
          </tbody>
        </table>
      </div>
    </section>

    <!-- DAILY AUTOMATED PRODUCT REVIEW ARTICLES -->
    <section id="daily-reviews" class="grey-section">
      <h2 class="section-title">Daily Hands-On Product Reviews &amp; Appliance Runtime Guides</h2>
      <p class="section-sub">Our automated engineering pipeline publishes <strong>3 brand-new product review &amp; load-testing articles every day</strong>. Currently indexing <strong>{len(all_articles)}</strong> comprehensive reviews:</p>
      <div id="dailyArticlesGrid" class="articles-grid">
        {articles_html}
      </div>
    </section>

    <!-- FAQ SECTION -->
    <section id="faq" class="grey-section">
      <h2 class="section-title">Frequently Asked Questions (Solar &amp; Battery Sizing FAQ)</h2>
      <p class="section-sub">Essential electrical formulas and buying rules for home backup, RV solar, and emergency preparedness.</p>
      {faq_html}
    </section>

  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="#calculator">Power Calculator</a>
        <a href="#search-section">Product Search</a>
        <a href="#bestsellers">Best Sellers</a>
        <a href="#comparison">Comparison Table</a>
        <a href="#daily-reviews">Daily Reviews</a>
        <a href="#faq">FAQ</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p style="margin-bottom:8px;"><strong>Affiliate Disclosure:</strong> WattGridCalc is a participant in the Amazon Services LLC Associates Program (Affiliate StoreID: <code>{AFFILIATE_TAG}</code>), an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com.</p>
      <p>&copy; {datetime.datetime.now(datetime.timezone.utc).year} WattGridCalc. Automatically updated daily via GitHub Actions.</p>
    </div>
  </footer>

  <script>
    var CATALOG_PRODUCTS = {products_js_json};
    var AFFILIATE_TAG = "{AFFILIATE_TAG}";

    function applyPreset(watts, hours, surge, voltage) {{
      document.getElementById('calcWatts').value = watts;
      document.getElementById('calcHours').value = hours;
      document.getElementById('calcSurgeFactor').value = surge.toString();
      document.getElementById('calcVoltage').value = voltage.toString();
      runPowerCalculator();
    }}

    function runPowerCalculator() {{
      var watts = parseFloat(document.getElementById('calcWatts').value) || 100;
      var hours = parseFloat(document.getElementById('calcHours').value) || 1;
      var surgeFactor = parseFloat(document.getElementById('calcSurgeFactor').value) || 2.0;
      var voltage = parseFloat(document.getElementById('calcVoltage').value) || 12.8;
      var sunHours = parseFloat(document.getElementById('calcSunHours').value) || 4.5;

      var rawWh = watts * hours;
      var requiredWh = Math.ceil(rawWh / 0.85);
      var requiredAh = Math.ceil(requiredWh / voltage);
      var surgeWatts = Math.ceil(watts * surgeFactor);
      var recommendedSolarW = Math.ceil(requiredWh / (sunHours * 0.8));

      document.getElementById('resWh').textContent = requiredWh.toLocaleString() + ' Wh';
      document.getElementById('resAh').textContent = requiredAh.toLocaleString() + ' Ah';
      document.getElementById('resInverter').textContent = surgeWatts.toLocaleString() + ' W';
      document.getElementById('resSolar').textContent = recommendedSolarW.toLocaleString() + ' W';

      // Find best matching product from catalog
      var sorted = CATALOG_PRODUCTS.slice().sort(function(a, b) {{ return a.wh - b.wh; }});
      var match = sorted.find(function(p) {{
        return p.wh >= requiredWh && p.watts >= watts;
      }}) || sorted[sorted.length - 1];

      var customQuery = encodeURIComponent('LiFePO4 Portable Power Station ' + requiredWh + 'Wh ' + watts + 'W Solar Generator');
      var customAmazonUrl = 'https://www.amazon.com/s?k=' + customQuery + '&tag=' + AFFILIATE_TAG;

      var recHtml = '<h4>✅ Recommended Hardware Match: ' + match.name + ' (' + match.badge + ')</h4>' +
        '<p style="font-size:0.9rem; color:#374151; margin-bottom:10px;">Provides <strong>' + match.wh + 'Wh capacity</strong> and <strong>' + match.watts + 'W output (' + match.surge + 'W surge)</strong> — ' + match.highlight + '</p>' +
        '<div style="display:flex; gap:10px; flex-wrap:wrap;">' +
        '<a class="btn-amazon" href="' + match.url + '" target="_blank" rel="nofollow sponsored noopener">Check ' + match.name + ' Price on Amazon &rarr;</a>' +
        '<a class="btn-outline" href="' + customAmazonUrl + '" target="_blank" rel="nofollow sponsored noopener">Browse All ' + requiredWh + 'Wh+ Systems on Amazon</a>' +
        '</div>';

      document.getElementById('calcRecommendationBox').innerHTML = recHtml;
    }}

    function filterCatalog() {{
      var q = (document.getElementById('productSearchInput').value || '').toLowerCase().trim();
      var cat = document.getElementById('categoryFilter').value;
      var cards = document.querySelectorAll('#productGridContainer .product-card');
      var visible = 0;

      cards.forEach(function(card) {{
        var nameData = card.getAttribute('data-name') || '';
        var cardCat = card.getAttribute('data-category') || '';
        var matchQ = !q || nameData.indexOf(q) !== -1;
        var matchCat = (cat === 'ALL') || (cardCat === cat);

        if (matchQ && matchCat) {{
          card.style.display = 'flex';
          visible++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      // Also filter Daily Review cards
      var artCards = document.querySelectorAll('#dailyArticlesGrid .article-card');
      artCards.forEach(function(ac) {{
        var sData = ac.getAttribute('data-article-search') || '';
        ac.style.display = (!q || sData.indexOf(q) !== -1) ? 'flex' : 'none';
      }});

      document.getElementById('searchCountStatus').textContent =
        'Showing ' + visible + ' matching flagship product(s) (and filtered daily review articles below):';
    }}

    function directAmazonSearch() {{
      var q = document.getElementById('productSearchInput').value.trim() || 'LiFePO4 Portable Power Station Solar Generator';
      var url = 'https://www.amazon.com/s?k=' + encodeURIComponent(q) + '&tag=' + AFFILIATE_TAG;
      window.open(url, '_blank');
    }}

    // Initialize calculator on page load
    runPowerCalculator();
  </script>
</body>
</html>"""


def generate_sitemap_and_rss(all_articles: list[dict]) -> list[str]:
    """Menghasilkan sitemap.xml, robots.txt, feed.xml, dan file verifikasi IndexNow."""
    today_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    urls = [f"{BASE_URL}/index.html"]

    sitemap_items = f"""  <url>
    <loc>{BASE_URL}/index.html</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>\n"""

    for art in all_articles:
        u = f"{BASE_URL}/reviews/{art['slug']}.html"
        urls.append(u)
        sitemap_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{art['date']}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)

    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)

    # RSS 2.0 Feed (untuk auto-syndication & crawler discovery)
    rss_items = ""
    for art in all_articles[:30]:
        u = f"{BASE_URL}/reviews/{art['slug']}.html"
        rss_items += f"""    <item>
      <title><![CDATA[{art['title']}]]></title>
      <link>{u}</link>
      <guid>{u}</guid>
      <pubDate>{art['date']}T06:00:00Z</pubDate>
      <description><![CDATA[Hands-on load test and runtime calculator for the {art['brand']} {art['model_name']} ({art['wh']}Wh / {art['watts']}W) powering {art['app_title']}.]]></description>
    </item>\n"""

    rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>WattGridCalc — Daily Solar &amp; Backup Power Reviews</title>
    <link>{BASE_URL}/index.html</link>
    <description>Automated daily engineering reviews and sizing calculators for portable power stations, LiFePO4 batteries, and UPS units.</description>
    <language>en-us</language>
{rss_items}  </channel>
</rss>"""

    with open(os.path.join(OUTPUT_DIR, "feed.xml"), "w", encoding="utf-8") as f:
        f.write(rss_xml)

    # IndexNow key verification file
    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

    return urls


def ping_indexnow(newly_added: list[dict]):
    """Mengirimkan URL baru secara otomatis ke IndexNow API agar mesin pencari langsung mengindeks artikel harian."""
    host = urllib.parse.urlparse(BASE_URL).netloc
    url_list = [f"{BASE_URL}/index.html", f"{BASE_URL}/sitemap.xml"]
    for art in newly_added:
        url_list.append(f"{BASE_URL}/reviews/{art['slug']}.html")

    payload = json.dumps({
        "host": host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": url_list
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[IndexNow] Successfully pinged {len(url_list)} URLs (HTTP {resp.status})")
    except Exception as exc:
        print(f"[IndexNow] Ping notice (non-blocking): {exc}")


def main():
    os.makedirs(REVIEWS_DIR, exist_ok=True)
    all_articles, newly_added = load_and_advance_state()

    # Build Homepage
    index_html = build_index_page(all_articles)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # Build Every Review Article Page
    for art in all_articles:
        page_html = build_article_page(art, all_articles)
        out_path = os.path.join(REVIEWS_DIR, f"{art['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)

    # Build Sitemap, Robots.txt, RSS Feed & IndexNow Key
    generate_sitemap_and_rss(all_articles)
    ping_indexnow(newly_added)

    print(f"Build complete! Total articles live: {len(all_articles)} (+{len(newly_added)} added today).")


if __name__ == "__main__":
    main()
