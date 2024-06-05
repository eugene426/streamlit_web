import streamlit as st

st.title('streamlit git과 연동시키는 방법 MEMO')

code = '''
conda activate streamlit_deploy ## 실행시켜주기
streamlit run app.py # 홈페이지 확인

# 이후 control+C를 눌러서 run streamlit 정지


## git에 commit하는 방법
gid add.
git commit # 상단에 제목 써주기 #:wq!로 저장

git push origin main 하면 제대로 업로드 댐!
'''

st.code(code,language='python')