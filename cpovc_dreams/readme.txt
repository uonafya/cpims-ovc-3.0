cpims=# +\d dreams*
                         Table "public.dreams_interventions"
         Column          |           Type           | Collation | Nullable | Default 
-------------------------+--------------------------+-----------+----------+---------
 intervention_id         | uuid                     |           | not null | 
 dreams_id               | character varying(15)    |           | not null | 
 cpims_id                | integer                  |           |          | 
 nemis_no                | character varying(15)    |           |          | 
 bcert_no                | character varying(25)    |           |          | 
 county_code             | integer                  |           |          | 
 county_name             | character varying(50)    |           |          | 
 sub_county_code         | integer                  |           |          | 
 sub_county_name         | character varying(70)    |           |          | 
 ward_code               | integer                  |           |          | 
 ward_name               | character varying(70)    |           |          | 
 intervention_date       | date                     |           |          | 
 intervention_type_code  | character varying(70)    |           |          | 
 intervention_type_name  | character varying(100)   |           |          | 
 hts_result              | character varying(100)   |           |          | 
 no_of_sessions_attended | character varying(10)    |           |          | 
 pregnancy_test_result   | character varying(15)    |           |          | 
 timestamp_created       | timestamp with time zone |           | not null | 
