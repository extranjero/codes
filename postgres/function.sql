CREATE OR REPLACE FUNCTION init_groups(fleet_schema TEXT, user_id TEXT) 
RETURNS void AS $$
DECLARE
schema_name TEXT;
BEGIN
  schema_name := fleet_schema || '.groups';
  EXECUTE format(E'INSERT INTO %s (id, name, active, created_by, updated_by) VALUES
	(700, \'%s\', true, \'%s\', \'%s\');', schema_name, 'Admin', user_id, user_id);
END;
$$ LANGUAGE plpgsql;

