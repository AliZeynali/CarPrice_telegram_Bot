CREATE TABLE users
(
  chat_id bigint NOT NULL,
  current character varying(20),
  brand character varying(20),
  model character varying(20),
  year integer,
  drived integer,
  nationality character varying(20),
  listlevel integer DEFAULT 0,
  pricesearchlevel integer DEFAULT 0,
  pricetype integer,
  banned boolean DEFAULT false,
  CONSTRAINT users_pkey PRIMARY KEY (chat_id)
)