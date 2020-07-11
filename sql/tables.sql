CREATE TABLE crm_events (
  date_received DATE
  ,product VARCHAR
  ,sub_product VARCHAR
  ,issue VARCHAR
  ,sub_issue VARCHAR
  ,consumer_complaint_narrative VARCHAR
  ,tags VARCHAR
  ,consumer_consent_provided VARCHAR
  ,submitted_via VARCHAR
  ,date_sent_to_company DATE
  ,company_response_to_consumer VARCHAR
  ,timely_response BOOLEAN
  ,consumer_disputed BOOLEAN
  ,complaint_id VARCHAR
  ,client_id VARCHAR
);

CREATE TABLE crm_call_center_logs (
  date_received DATE
  ,complaint_id VARCHAR
  ,rand_client VARCHAR
  ,phone_final VARCHAR
  ,vru_line VARCHAR
  ,call_id INT
  ,priority VARCHAR
  ,type VARCHAR
  ,outcome VARCHAR
  ,server VARCHAR
  ,ser_start TIME
  ,ser_exit TIME
  ,ser_time TIME
);

-- COPY crm_call_center_logs FROM '${PATH}/dkatalis-take-home-test-bi-analyst/datasets/crm_call_center_logs.csv' CSV HEADER;
