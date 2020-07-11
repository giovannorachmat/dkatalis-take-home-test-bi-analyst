with raw_events as (
  select
    *
  from
    crm_events
)
,raw_logs as (
  select
    date_received
    ,complaint_id
    ,priority
    ,outcome
    ,ser_time
    ,ser_start
    ,ser_exit
  from
    crm_call_center_logs
)
,parse_all as (
  select
    a.*
    ,case
        when outcome is null then 'UNIDENTIFIED'
        else outcome
    end as outcome_tag
    ,consumer_disputed
    -- ,consumer_complaint_narrative
    ,company_response_to_consumer
    ,tags
    ,product
    ,issue
    ,client_id
  from
    raw_logs a
  left join
    raw_events b
    using(complaint_id)
)

select
    -- *
    tags
    -- ,round(avg(extract(epoch from ser_time)/60)::numeric,2) avg_response_time_minutes
    ,sum(extract(epoch from ser_time)/60)
from
  parse_all
group by
    1
order by
    2 desc,1
-- limit 10;
