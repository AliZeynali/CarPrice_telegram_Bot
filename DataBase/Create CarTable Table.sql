CREATE TABLE cartable
(
  brand character varying(20),
  model character varying(20),
  price bigint,
  drived bigint,
  madeyear integer,
  fueltype character varying(20),
  state character varying(20),
  color character varying(20),
  gear character varying(20),
  url character varying(500) NOT NULL,
  nationality character varying(20),
  date date,
  "time" time without time zone,
  perbrand character varying(15),
  permodel character varying(15),
  CONSTRAINT cartable_pkey PRIMARY KEY (url)
)