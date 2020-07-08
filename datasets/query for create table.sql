date_received date
,complaint_id varchar
,rand_client varchar
,phone_final varchar
,vru_line varchar
,call_id int
,priority varchar
,type varchar
,outcome varchar
,server varchar
,ser_start time
,ser_exit time
,ser_time time

create table crm_events (
date_received date
,product varchar
,sub_product varchar
,issue varchar
,sub_issue varchar
,consumer_complaint_narrative varchar
,tags varchar
,consumer_consent_provided varchar
,submitted_via varchar
,date_sent_to_company date
,company_response_to_consumer varchar
,timely_response boolean
,consumer_disputed boolean
,complaint_id varchar
,client_id varchar
)
