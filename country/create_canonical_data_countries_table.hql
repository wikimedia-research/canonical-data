-- Create table statement for an static table about countries.
--
-- This table belongs to analytics-product
--
-- Parameters:
--     <none>
--
-- Usage
--     spark3-sql \
--       -f create_countries_table.hql   \
--       --database canonical_data
--

CREATE TABLE IF NOT EXISTS `countries` (
     name               STRING  COMMENT 'Country name, aligned with the article on English Wikipedia',
     iso_code           STRING  COMMENT 'ISO 3166-1 two-letter country code',
     economic_region    STRING  COMMENT 'Global South/North, according to [[en:Global North and Global South]]',
     maxmind_continent  STRING  COMMENT 'Continent, according to MaxMind databases',
     is_protected       BOOLEAN COMMENT 'Whether the country appears in [[wikitech:Country_protection_list]]',
     is_eu              BOOLEAN COMMENT 'Whether the country belongs to the European Union'
)
COMMENT 'Metadata information about countries we release data about.'
USING parquet;
