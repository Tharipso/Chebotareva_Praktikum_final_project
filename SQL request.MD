
ЗАДАНИЕ 1
select "Couriers"."login", count("Orders"."inDelivery")
from "Couriers" join "Orders" on "Couriers"."id"="Orders"."courierId" 
where "Orders"."inDelivery" = TRUE
group by "Couriers"."id";


ЗАДАНИЕ 2
select track,
    CASE 
    when finished = true then '2' 
    when canсelled = true then '-1'
    when inDelivery = true then '1'
    else '0'
    end status
from "Orders";




