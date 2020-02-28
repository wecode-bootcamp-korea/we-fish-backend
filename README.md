# Introduction

website clone project (https://www.onul-hoi.com)
By 6 developers (4 Front-End, 2 Back-End)



# DB modeling
![오늘회333_20200228_08_15](https://user-images.githubusercontent.com/58175076/75519012-9e1a7a00-5a45-11ea-95ff-abe66d71a85a.png)

&nbsp;
&nbsp;
&nbsp;
## 회원 관련 테이블

&nbsp;
### users
- 가입 회원의 정보를 저장합니다.
- 외부 실명인증을 통해 생년월일을 저장합니다.

&nbsp;
### user_qnas
- 1:1문의에 대한 기록을 남깁니다.


&nbsp;
&nbsp;
&nbsp;
## 상품 관련 테이블

&nbsp;
### categories
- 상품 카테고리 정보를 저장합니다.
- 카테고리 목록에 표시되는 카테고리인지 여부가 BOOLEAN 필드로 구분됩니다. 

&nbsp;
### products
- 상품의 정보를 저장합니다.
- 카테고리와 MANY TO MANY 관계를 이룹니다.
- 상세설명은 html 태그로 되어 있습니다.
- 상품 등록일이 7일 이내일일 경우 신상품 카테고리로 구분됩니다.

&nbsp;
### products_categories
- 상품과 카테고리의 관계정보를 저장합니다.
- 상품과 카테고리는 외부키를 가져옵니다. 

&nbsp;
### sort_keywords
- 상품의 정렬 순서를 저장합니다.
- 연결 관계가 없는 별도의 테이블로 관리합니다.

&nbsp;
### dates
- 상품 배송이 가능한 날짜를 저장합니다.
- 오늘 이후 5일을 도착 날짜포 표시할 수 있습니다.

&nbsp;
### stocks
- 상품의 날짜별 배송가능 수량을 저장합니다.
- 상품과 날짜는 외부키를 가져옵니다.
- 상품의 날짜별 수량이 없어지면 배송가능 날짜가 다음날로 바뀝니다.

&nbsp;
### sections
- themes 의 상위 카테고리
- 각 테마의 조합을 저장합니다.

&nbsp;
### themes
- 테마 정보를 저장합니다.

&nbsp;
### themeproducts
- 테마의 상품 구성을 저장합니다.
- 상품은 외부키로 가져옵니다.

&nbsp;
### reviews
- 상품별 상품후기를 저장합니다.
- 상품명, 작성자, 주문번호는 외부키를 가져옵니다.
- 상품별 후기를 가져올 수 있습니다.
- 주문번호에 해당하는 후기를 가져올 수 있습니다.

&nbsp;
&nbsp;
&nbsp;


## 주문 관련 테이블

&nbsp;
### carts
- 장바구니 정보를 저장합니다.
- 주문번호를 외부키로 가지며 장바구니에 상품을 넣으면 `orders`에 주문번호가 자동으로 생성됩니다.

&nbsp;
### orders
- 장바구니에서 결제하기를 누를 경우 장바구니의 상품 정보를 그대로 가져옵니다.
- 상품 목록과 주문 금액 그리고 결제방법, 배송 정보를 저장합니다.
- status 칼럼에서 주문완료 여부를 구분합니다.
- `carts` 테이블과 조인하면 상품별 누적판매 수량으로 인기상품 정렬할 수 있습니다.


&nbsp;
### addresses
- 배송 가능 지역 목록을 저장합니다.
- 회원가입시, 배송지 변경시 우편번호로 배송 가능 여부를 판단할 수 있습니다.

