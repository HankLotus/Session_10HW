import streamlit as st
import time

topping_price = 5,5,6,7,8,10    # giá từng loại topping
topping_list = 'Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau câu (6K)',  'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)'

st.title('Trà sữa CoTAI')
size = st.radio('Kích cỡ', ('Nhỏ (30K)', 'Vừa (40K)', 'Lớn (50K)'), horizontal=True)
st.write('Thêm')
col1, col2, col3, col4 = st.columns(4)

with col1:
  milk = st.checkbox('Sữa (5K)')
with col2:
  cafe = st.checkbox('Cà phê (8K)')
with col3:
  cream = st.checkbox('Kem (10K)')
with col4:
  Egg = st.checkbox('Trứng (15K)')
topping = st.multiselect('Topping', topping_list)
n = st.number_input('Số lượng', min_value=1, max_value=100, step=1)
Text = st.text_input('Ghi chú', 'Ít đá, nhiều sữa, shipper đẹp trai')


if st.button('Đặt hàng'):
  with st.spinner('Vui lòng chờ ...'):
    time.sleep(2) # processing simulator
    st.write(n, size, milk, cafe, topping)
    if size== 'Nhỏ (30K)':
        price=30
    elif size== 'Vừa (40K)':
        price=40
    else:
        price==50
    price = 30 if size == 'Nhỏ (30K)' else 40
    topping_money=0
    for i in range(len(topping_list)):
        if topping_list[i] in topping:
            topping_money += topping_price[i]
    money = n * (price + milk*5 + cafe*8 + cream*10 + Egg*15 + topping_money)
    st.success('Thành tiền: '  + str(money) + 'K')
    st.balloons()