import mysql.connector

# @st.cache(hash_funcs={_mysql_connector.MySQL: my_hash_func})

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swapna2021",
    database = "ecomm"
)

getOrderStatusDf = "SELECT * FROM ecomm.order_status"

getOrdersDf = "SELECT * FROM ecomm.orders"

# todayOrdersDetails = "SELECT DATE(order_submit_dt_tm) as 'Date', order_id, total_amount FROM ecomm.orders WHERE DATE(order_submit_dt_tm) = CURDATE()"

todayOrdersDetails = "SELECT DATE(order_submit_dt_tm) as 'Date', ROUND(COUNT(order_id)) as 'Count', ROUND(SUM(IFNULL(total_amount, 0))) as 'Amount' FROM ecomm.orders WHERE DATE(order_submit_dt_tm) = CURDATE()"

averageOrdersBy30Days = "SELECT DATE(order_submit_dt_tm) as 'Date', ROUND(COUNT(order_id)/COUNT(DISTINCT DATE(order_submit_dt_tm))) as 'Count', ROUND(AVG(total_amount)) as 'Amount' FROM ecomm.orders WHERE DATE(order_submit_dt_tm) >= (CURDATE()- INTERVAL 1 MONTH)"

orderCountByStatus = "SELECT DATE(order_track_update_time) as 'Date', status_cd, order_id FROM ecomm.order_status WHERE order_status.order_track_update_time != 0"

filterOrderStatusDf = "SElECT order_id, status_cd, estimated_time FROM ecomm.order_status"

ordersCount = "SELECT COUNT(order_id) as 'No Of Orders', order_id, DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' FROM ecomm.orders GROUP BY DATE(order_submit_dt_tm)" 

currentMonthOrders = "SELECT COUNT(order_id) as 'No Of Orders', order_id, coupon_applied, DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' FROM ecomm.orders WHERE MONTH(order_submit_dt_tm) = MONTH(CURDATE() - INTERVAL 1 MONTH) GROUP BY DATE(order_submit_dt_tm)"

unShippedordersWeekCount = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as Date, DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped') AND o.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 1 WEEK)) GROUP BY DATE(order_submit_dt_tm)"

unShippedordersByDaysCount = "select DATE(order_submit_dt_tm) as 'Date', order_id, COUNT(order_id) as 'No Of Orders' from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped') AND o.order_submit_dt_tm >= ( CURDATE() - INTERVAL 10 DAY ) GROUP BY Date"

ordersLastMonthCount = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from ecomm.orders where orders.order_submit_dt_tm >= ( CURDATE() - INTERVAL 1 MONTH) GROUP BY DATE(order_submit_dt_tm)"

ordersLastdaysCount = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from ecomm.orders where orders.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 10 DAY)) GROUP BY DATE(order_submit_dt_tm)"

ordersCountByCoupon = "select coupon_applied, count(order_id) as 'No Of Orders' from ecomm.orders where orders.coupon_applied <> '0' GROUP BY coupon_applied"

unShippedordersMonthCount = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped') AND o.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 1 MONTH)) GROUP BY DATE(order_submit_dt_tm)"

unShippedOrdersMonthCount1 = "select DATE(order_submit_dt_tm) as 'Date', status_cd, customer_id from orders o, order_status os WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped') GROUP BY order_submit_dt_tm"

ordersCountByTotalAmount5 = "select COUNT(order_id) as 'No Of Orders' from ecomm.orders where orders.total_amount > 1000"

ordersCountByTotalAmount4 = "select COUNT(order_id) as 'No Of Orders' from ecomm.orders where orders.total_amount > 500 and orders.total_amount >= 1000"

ordersCountByTotalAmount3 = "select COUNT(order_id) as 'No Of Orders' from ecomm.orders where orders.total_amount > 300 and orders.total_amount >= 500"

ordersCountByTotalAmount2 = "select COUNT(order_id) as 'No Of Orders' from ecomm.orders where orders.total_amount > 100 and orders.total_amount >= 300"

ordersCountByTotalAmount1 = "select COUNT(order_id) as 'No Of Orders' from ecomm.orders where orders.total_amount <= 100"
