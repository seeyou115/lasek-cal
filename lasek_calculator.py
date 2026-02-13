import streamlit as st

# 페이지 설정
st.set_page_config(page_title="라섹 수술 계산기", page_icon="👁️", layout="centered")

# 제목
st.title("👁️ 라섹 수술 노모그램 계산기")
st.markdown("---")

# 설명
st.markdown("""
### 사용 방법
환자의 굴절 수치를 입력하시면 노모그램에 따라 조정된 절삭 수치를 자동으로 계산합니다.
""")

# 입력 섹션
col1, col2 = st.columns(2)

with col1:
    sph_input = st.number_input(
        "SPH (구면렌즈 도수)", 
        min_value=-15.0, 
        max_value=5.0, 
        value=0.0, 
        step=0.25,
        format="%.2f"
    )

with col2:
    cyl_input = st.number_input(
        "CYL (난시 도수)", 
        min_value=-10.0, 
        max_value=0.0, 
        value=0.0, 
        step=0.25,
        format="%.2f"
    )

st.markdown("---")

# 계산 버튼
if st.button("🔍 절삭 수치 계산", type="primary", use_container_width=True):
    
    # 초기값: 입력값 그대로
    adjusted_sph = sph_input
    adjustment = 0.0
    reason = "조정 없음"
    
    # 노모그램 로직 (절차적으로 단계별 확인)
    
    # 1단계: SPH가 0인 경우
    if sph_input == 0:
        if -5.0 <= cyl_input <= -0.25:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = "SPH=0, CYL이 -0.25~-5.0 범위"
        else:
            reason = "SPH=0, CYL이 범위 밖"
    
    # 2단계: SPH가 -0.25 ~ -0.75인 경우
    elif -0.75 <= sph_input <= -0.25:
        if -5.0 <= cyl_input <= -0.25:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = f"SPH={sph_input}, CYL이 -0.25~-5.0 범위"
        else:
            reason = f"SPH={sph_input}, CYL이 범위 밖"
    
    # 3단계: SPH가 -1.00 ~ -1.25인 경우
    elif -1.25 <= sph_input <= -1.00:
        if -4.75 <= cyl_input <= -0.25:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = f"SPH={sph_input}, CYL이 -0.25~-4.75 범위"
        else:
            reason = f"SPH={sph_input}, CYL이 범위 밖"
    
    # 4단계: SPH가 -1.50인 경우
    elif sph_input == -1.50:
        if -4.5 <= cyl_input <= -0.25:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = "SPH=-1.50, CYL이 -0.25~-4.5 범위"
        else:
            reason = "SPH=-1.50, CYL이 범위 밖"
    
    # 5단계: SPH가 -1.75인 경우
    elif sph_input == -1.75:
        if -4.25 <= cyl_input <= -0.25:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = "SPH=-1.75, CYL이 -0.25~-4.25 범위"
        else:
            reason = "SPH=-1.75, CYL이 범위 밖"
    
    # 6단계: SPH가 -2.00인 경우
    elif sph_input == -2.00:
        if -4.0 <= cyl_input <= -0.25:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = "SPH=-2.00, CYL이 -0.25~-4.0 범위"
        else:
            reason = "SPH=-2.00, CYL이 범위 밖"
    
    # 7단계: SPH가 -2.25인 경우
    elif sph_input == -2.25:
        if -3.5 <= cyl_input <= -0.25:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = "SPH=-2.25, CYL이 -0.25~-3.5 범위"
        else:
            reason = "SPH=-2.25, CYL이 범위 밖"
    
    # 8단계: SPH가 -2.50인 경우
    elif sph_input == -2.50:
        if -2.75 <= cyl_input <= -1.00:
            adjustment = -0.25
            adjusted_sph = sph_input - 0.25
            reason = "SPH=-2.50, CYL이 -1.00~-2.75 범위"
        else:
            reason = "SPH=-2.50, CYL이 범위 밖"
    
    # 9단계: SPH가 -2.75 ~ -4.50인 경우
    elif -4.50 <= sph_input <= -2.75:
        reason = f"SPH={sph_input}, CYL 상관없이 조정 없음"
    
    # 10단계: SPH가 -4.75인 경우
    elif sph_input == -4.75:
        if cyl_input >= -5.75:
            adjustment = 0.25
            adjusted_sph = sph_input + 0.25
            reason = "SPH=-4.75, CYL이 -5.75 이상"
        else:
            reason = "SPH=-4.75, CYL이 범위 밖"
    
    # 11단계: SPH가 -5.00인 경우
    elif sph_input == -5.00:
        if cyl_input >= -5.00:
            adjustment = 0.25
            adjusted_sph = sph_input + 0.25
            reason = "SPH=-5.00, CYL이 -5.00 이상"
        else:
            reason = "SPH=-5.00, CYL이 범위 밖"
    
    # 12단계: SPH가 -5.25인 경우
    elif sph_input == -5.25:
        if cyl_input >= -3.75:
            adjustment = 0.25
            adjusted_sph = sph_input + 0.25
            reason = "SPH=-5.25, CYL이 -3.75 이상"
        else:
            reason = "SPH=-5.25, CYL이 범위 밖"
    
    # 13단계: SPH가 -5.50 ~ -6.50인 경우
    elif -6.50 <= sph_input <= -5.50:
        adjustment = 0.25
        adjusted_sph = sph_input + 0.25
        reason = f"SPH={sph_input}, CYL 상관없이 +0.25"
    
    # 14단계: SPH가 -6.75인 경우
    elif sph_input == -6.75:
        if cyl_input <= -5.00:
            adjustment = 0.25
            adjusted_sph = sph_input + 0.25
            reason = "SPH=-6.75, CYL이 -5.00 이하"
        else:
            adjustment = 0.50
            adjusted_sph = sph_input + 0.50
            reason = "SPH=-6.75, CYL이 -5.00 초과"
    
    # 15단계: SPH가 -7.00인 경우
    elif sph_input == -7.00:
        if cyl_input <= -3.75:
            adjustment = 0.25
            adjusted_sph = sph_input + 0.25
            reason = "SPH=-7.00, CYL이 -3.75 이하"
        else:
            adjustment = 0.50
            adjusted_sph = sph_input + 0.50
            reason = "SPH=-7.00, CYL이 -3.75 초과"
    
    # 16단계: SPH가 -7.25 ~ -7.75인 경우
    elif -7.75 <= sph_input <= -7.25:
        adjustment = 0.50
        adjusted_sph = sph_input + 0.50
        reason = f"SPH={sph_input}, CYL 상관없이 +0.50"
    
    # 17단계: SPH가 -8.00인 경우
    elif sph_input == -8.00:
        if cyl_input <= -4.75:
            adjustment = 0.50
            adjusted_sph = sph_input + 0.50
            reason = "SPH=-8.00, CYL이 -4.75 이하"
        else:
            adjustment = 0.75
            adjusted_sph = sph_input + 0.75
            reason = "SPH=-8.00, CYL이 -4.75 초과"
    
    # 18단계: SPH가 -8.25인 경우
    elif sph_input == -8.25:
        if -2.75 <= cyl_input <= -1.00:
            adjustment = 0.50
            adjusted_sph = sph_input + 0.50
            reason = "SPH=-8.25, CYL이 -1.00~-2.75"
        else:
            adjustment = 0.75
            adjusted_sph = sph_input + 0.75
            reason = "SPH=-8.25, CYL이 범위 밖"
    
    # 19단계: SPH가 -8.50 ~ -9.50인 경우
    elif -9.50 <= sph_input <= -8.50:
        adjustment = 0.75
        adjusted_sph = sph_input + 0.75
        reason = f"SPH={sph_input}, CYL 상관없이 +0.75"
    
    # 20단계: SPH가 -9.75 ~ -10.25인 경우
    elif -10.25 <= sph_input <= -9.75:
        adjustment = 1.00
        adjusted_sph = sph_input + 1.00
        reason = f"SPH={sph_input}, CYL 상관없이 +1.00"
    
    # 결과 출력
    st.success("✅ 계산 완료!")
    
    # 결과 박스
    result_col1, result_col2, result_col3 = st.columns(3)
    
    with result_col1:
        st.metric(label="입력 SPH", value=f"{sph_input:.2f}")
    
    with result_col2:
        st.metric(label="조정값", value=f"{adjustment:+.2f}" if adjustment != 0 else "0.00")
    
    with result_col3:
        st.metric(label="절삭 SPH", value=f"{adjusted_sph:.2f}", delta=f"{adjustment:+.2f}" if adjustment != 0 else None)
    
    st.info(f"📋 적용 규칙: {reason}")
    
    # CYL은 그대로
    st.markdown("---")
    st.markdown(f"**CYL (난시 도수)**: {cyl_input:.2f} → **{cyl_input:.2f}** (변경 없음)")

# 하단 안내
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.9em;'>
    <p>⚠️ 본 계산기는 참고용입니다. 실제 수술 시 의사의 판단이 최우선입니다.</p>
</div>
""", unsafe_allow_html=True)
