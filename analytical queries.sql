with raw_events as (
  select
    date_received
    ,product
    ,issue
    ,complaint_id
    ,client_id
  from
    crm_events
)
,raw_logs as (
  select
    date_received
    ,complaint_id
    ,priority
    ,type
    ,outcome
    ,server
    ,ser_time
  from
    crm_call_center_logs
)
,parse_all as (
  select
    a.date_received
    ,a.complaint_id
    ,b.client_id
    ,issue
    ,product
    ,priority
    ,type
    ,outcome
    ,server
    ,ser_time
  from
    raw_logs a
  left join
    raw_events b
    using(complaint_id)
)

select
  *
from
  parse_all
limit 10;

/*
select
    date_trunc('month',date_received) as month
    ,product
    ,round(avg(ser_time),2) as avg_complaints
    ,count(distinct complaint_id) as complaints
    ,count(distinct client_id) as users
    ,round(sum(complaints)/sum(users),2) as complaint_rate
    ,round(avg(complaints),2) as avg_complaints
    ,round(avg(users),2) as avg_users
from
    raw
group by
    1,2
order by
    1,2 */
