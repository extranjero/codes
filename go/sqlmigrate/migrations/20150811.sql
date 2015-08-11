-- +migrate Up

--Groups (Roles)
CREATE TABLE IF NOT EXISTS groups (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	created_by UUID,
	updated_by UUID,
	active BOOLEAN DEFAULT TRUE
);
--Controller name
CREATE TABLE IF NOT EXISTS resources (
	id SERIAL PRIMARY KEY,
	res_name TEXT UNIQUE NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	created_by UUID,
	updated_by UUID,
	active BOOLEAN DEFAULT TRUE
);
--Controller actions
CREATE TABLE IF NOT EXISTS actions (
	id SERIAL PRIMARY KEY,
	res_id INT REFERENCES resources(id),
	action_name TEXT NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	created_by UUID,
	updated_by UUID,
	active BOOLEAN DEFAULT TRUE

);
--Access Control Resource
CREATE TABLE IF NOT EXISTS acrs (
	id SERIAL PRIMARY KEY,
	grp_id INT REFERENCES groups(id),
	res_id INT REFERENCES resources(id),
	created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	created_by UUID,
	updated_by UUID,
	active BOOLEAN DEFAULT TRUE

);

--Acess Control Resource Permissions for actions
CREATE TABLE IF NOT EXISTS acr_perms (
	id SERIAL PRIMARY KEY,
	acr_id INT REFERENCES acrs(id),
	action_id INT REFERENCES actions(id),
	perm bool DEFAULT TRUE,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	created_by UUID,
	updated_by UUID,
	active BOOLEAN DEFAULT TRUE
);

-- +migrate Down 
DROP TABLE IF EXISTS actions CASCADE;
DROP TABLE IF EXISTS acrs CASCADE;
DROP TABLE IF EXISTS groups CASCADE;
DROP TABLE IF EXISTS resources CASCADE;
DROP TABLE IF EXISTS acr_perms CASCADE;
