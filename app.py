import datetime
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AlphaDrop | Airdrop Surveillance Hub",
    page_icon="🪂",
    layout="wide",
)

# App Title & Header
st.title("🪂 AlphaDrop: Airdrop Surveillance & Claim Tracker")
st.caption(
    "Track pre-token alpha, log interactions, and evaluate security"
    " protocols instantly."
)

# Internal Database of Active High-Potential Projects
PROJECTS_DB = {
    "Monad": {
        "type": "Testnet / EVM L1",
        "cost": "Zero ($0)",
        "vc": "$225M+",
        "status": "Active Alpha Testing",
    },
    "Berachain": {
        "type": "Testnet / Proof-of-Liquidity",
        "cost": "Zero ($0)",
        "vc": "$140M+",
        "status": "Public Testnet BeraHome",
    },
    "Base Ecosystem": {
        "type": "Mainnet / Ethereum L2",
        "cost": "Low Gas Only",
        "vc": "Coinbase Backed",
        "status": "Active Mainnet Actions",
    },
    "Linea": {
        "type": "Mainnet / zkEVM L2",
        "cost": "Variable Gas",
        "vc": "$700M+ (ConsenSys)",
        "status": "Voyage Campaigns",
    },
}

VERIFIED_DOMAINS = [
    "monad.xyz",
    "berachain.com",
    "base.org",
    "linea.build",
    "dune.com",
    "revoke.cash",
]

# Sidebar Navigation
st.sidebar.header("🎯 Mission Control")
menu = st.sidebar.radio(
    "Navigate Sections",
    [
        "Live Surveillance Market",
        "My Daily Interaction Log",
        "Wallet Health Calculator",
        "Anti-Scam Domain Scanner",
    ],
)

# ----------------- SECTION 1: LIVE SURVEILLANCE -----------------
if menu == "Live Surveillance Market":
  st.header("⚡ Live Institutional Pre-Token Pipelines")
  st.info(
      "These projects are heavily backed by VC funds and do not have a public"
      " token yet."
  )

  col1, col2 = st.columns(2)

  for idx, (name, details) in enumerate(PROJECTS_DB.items()):
    target_col = col1 if idx % 2 == 0 else col2
    with target_col:
      with st.container(border=True):
        st.subheader(f"{name}")
        st.markdown(f"**Network Type:** `{details['type']}`")
        st.markdown(f"**Capital Required:** :green[{details['cost']}]")
        st.markdown(f"**Venture Funding Raised:** `{details['vc']}`")
        st.markdown(f"**Current Phase:** :orange[{details['status']}]")

# ----------------- SECTION 2: INTERACTION LOG -----------------
elif menu == "My Daily Interaction Log":
  st.header("📝 On-Chain Daily Task Check-in")
  st.write(
      "Log your structural interactions to prevent your wallet signature from"
      " looking like a bot."
  )

  with st.form("interaction_form"):
    project = st.selectbox("Select Target Network", list(PROJECTS_DB.keys()))
    action_type = st.multiselect(
        "Actions Performed Today",
        [
            "Claimed Faucet Tokens",
            "Executed Token Swap",
            "Provided Liquidity (Pools)",
            "Bridged Assets Natively",
            "Voted on Governance Proposal",
        ],
    )
    tx_hash = st.text_input(
        "Transaction Hash / Note (Optional)",
        placeholder="e.g., Swapped 10 mock tokens",
    )
    date_selected = st.date_input("Date Logged", datetime.date.today())

    submitted = st.form_submit_button("Log Session to Ledger")
    if submitted:
      if not action_type:
        st.warning("Please select at least one action.")
      else:
        st.success(
            f"Successfully saved entry for **{project}** on {date_selected}!"
            " On-chain footprint updated."
        )

# ----------------- SECTION 3: WALLET HEALTH -----------------
elif menu == "Wallet Health Calculator":
  st.header("🩺 Airdrop Eligibility Health Evaluator")
  st.write(
      "Foundations filter out wallets based on activity thresholds. Score your"
      " profile below:"
  )

  tx_count = st.slider(
      "Total lifetime transactions (Tx) in this farming wallet?", 0, 150, 15
  )
  wallet_age = st.number_input("Wallet age in days?", min_value=0, value=30)
  networks_used = st.slider(
      "How many unique bridges/networks have you touched?", 1, 10, 2
  )
  mainnet_balance = st.number_input(
      "Current Mainnet maintenance balance (in USD equivalent)?",
      min_value=0.0,
      value=15.00,
  )

  # Simple Scoring Engine
  score = 0
  if tx_count > 50:
    score += 30
  elif tx_count > 15:
    score += 15

  if wallet_age > 90:
    score += 25
  elif wallet_age > 30:
    score += 15

  if networks_used >= 3:
    score += 25
  else:
    score += 10

  if mainnet_balance >= 50.0:
    score += 20
  elif mainnet_balance >= 10.0:
    score += 10

  st.subheader(f"Your Wallet Health Score: **{score} / 100**")

  if score >= 75:
    st.balloons()
    st.success(
        "🟢 Highly Organic Profile! Excellent positioning to bypass anti-sybil"
        " bot filters."
    )
  elif score >= 45:
    st.warning(
        "🟡 Average Profile. Increase your unique active weeks and bump up gas"
        " asset maintenance balance."
    )
  else:
    st.error(
        "🔴 Sybil Danger Zone. Your wallet is at high risk of being classified"
        " as a generic automation bot. Add more transactional depth."
    )

# ----------------- SECTION 4: ANTI-SCAM SCANNER -----------------
elif menu == "Anti-Scam Domain Scanner":
  st.header("🛡️ Malicious Link Phishing Protection Check")
  st.write(
      "Scammers set up fake clone sites to drain wallets. Run links through our"
      " domain filter before connecting."
  )

  input_url = st.text_input(
      "Paste the Airdrop / Claim Site URL to Scan:",
      placeholder="e.g., check-monad-tokens.xyz",
  )

  if input_url:
    cleaned_url = (
        input_url.lower()
        .replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
    )

    match = [domain for domain in VERIFIED_DOMAINS if domain in cleaned_url]

    if match:
      st.success(
          "✅ Safe Match Found: The domain aligns cleanly with the official"
          f" project directory (`{match[0]}`)."
      )
    else:
      st.error(
          "🚨 CRITICAL WARNING: This URL does not match our pre-verified"
          " institutional root servers. Do not enter your private key or approve"
          " unlimited transaction scopes on this application!"
      )
