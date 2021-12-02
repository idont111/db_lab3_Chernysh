select * from rank_period;

create table rank_periodcopy as select * from rank_period; 
select * from rank_periodcopy;


DO $$
DECLARE
    period_id          rank_periodcopy.period_id%TYPE;
    rank_period_name   rank_periodcopy.rank_period_name%TYPE;
	

BEGIN
    period_id := '4o';
    rank_period_name := '2010-10-10';
	
    FOR counter IN 1..3
        LOOP
            INSERT INTO rank_periodcopy(period_id, rank_period_name)
    		VALUES (period_id || counter, rank_period_name + counter);
        END LOOP;
END;
$$
