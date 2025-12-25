import streamlit as st

# ページ設定
st.set_page_config(
    page_title="仕入れ利益計算機",
    page_icon="💰",
    layout="centered"
)

# タイトル
st.title("💰 仕入れ利益計算機")
st.write("物販の利益を簡単に計算できます！")

st.markdown("---")

# 入力欄
col1, col2 = st.columns(2)

with col1:
    cost_price = st.number_input(
        "🛒 仕入れ価格（円）",
        min_value=0,
        value=1000,
        step=100,
        help="商品の仕入れ価格を入力してください"
    )

with col2:
    selling_price = st.number_input(
        "💴 販売価格（円）",
        min_value=0,
        value=2000,
        step=100,
        help="販売予定価格を入力してください"
    )

# 販売先の選択
platform = st.selectbox(
    "🏪 販売先を選択",
    ["楽天市場", "Amazon", "Yahoo!ショッピング", "メルカリ"],
    help="販売するプラットフォームを選んでください"
)

# 各プラットフォームの手数料率
fee_rates = {
    "楽天市場": 10.0,
    "Amazon": 15.0,
    "Yahoo!ショッピング": 8.0,
    "メルカリ": 10.0
}

# 選択されたプラットフォームの手数料率
fee_rate = fee_rates[platform]

st.info(f"📊 {platform}の販売手数料: {fee_rate}%")

st.markdown("---")

# 計算ボタン
if st.button("🎯 利益を計算する", type="primary", use_container_width=True):
    
    # 手数料を計算
    fee = selling_price * (fee_rate / 100)
    
    # 利益を計算
    profit = selling_price - cost_price - fee
    
    # 利益率を計算（仕入れ価格に対する利益の割合）
    if cost_price > 0:
        profit_rate = (profit / cost_price) * 100
    else:
        profit_rate = 0
    
    # 結果表示
    st.markdown("---")
    st.subheader("📊 計算結果")
    
    # 3列で表示
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="💴 販売価格",
            value=f"{selling_price:,}円"
        )
    
    with col2:
        st.metric(
            label="💸 手数料",
            value=f"{int(fee):,}円",
            delta=f"-{fee_rate}%"
        )
    
    with col3:
        st.metric(
            label="🛒 仕入れ価格",
            value=f"{cost_price:,}円"
        )
    
    st.markdown("---")
    
    # 利益の表示（条件分岐）
    if profit > 0:
        st.success(f"### ✅ 利益: {int(profit):,}円")
        st.success(f"### 📈 利益率: {profit_rate:.1f}%")
        
        # 利益率に応じたメッセージ
        if profit_rate >= 30:
            st.balloons()  # 🎈アニメーション
            st.markdown("### 🔥🔥🔥 素晴らしい！高利益率です！")
        elif profit_rate >= 20:
            st.markdown("### 🎯 良い利益率です！")
        elif profit_rate >= 10:
            st.markdown("### 👍 まずまずの利益率です")
        else:
            st.markdown("### ⚠️ 利益率が低めです")
    
    elif profit == 0:
        st.warning("### ⚖️ 利益ゼロ（トントン）")
        st.write("利益も損失もありません")
    
    else:  # profit < 0
        st.error(f"### ❌ 赤字: {int(abs(profit)):,}円")
        st.error("### 📉 この条件では損失が出ます")
        st.write("💡 仕入れ価格を下げるか、販売価格を上げる必要があります")
    
    # 内訳を表示
    st.markdown("---")
    st.subheader("📋 計算の内訳")
    
    breakdown = f"""
    - 販売価格: **{selling_price:,}円**
    - 販売手数料 ({fee_rate}%): **-{int(fee):,}円**
    - 仕入れ価格: **-{cost_price:,}円**
    - ━━━━━━━━━━━━━━
    - **利益: {int(profit):,}円**
    - **利益率: {profit_rate:.1f}%**
    """
    
    st.markdown(breakdown)

# フッター
st.markdown("---")
st.caption("💡 ヒント: 利益率20%以上を目指すのがおすすめです")
st.caption("Created with ❤️ by Streamlit")
