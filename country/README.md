# canonical_data.countries

As of December 2023, this dataset contains records for the 249 territories included in [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) as well as one more included in [MaxMind](https://en.wikipedia.org/wiki/MaxMind), our [geolocation service](https://wikitech.wikimedia.org/wiki/Geolocation):

- Kosovo (ISO code `XK`)

## Fields

### `name`

> String: Distinct values

The country's common English name (generally the title chosen by the English Wikipedia for its article). This means, for example, using "Laos" rather than "Lao People's Democratic Republic" and "Bolivia" rather than "Bolivia (Plurinational State of)".

### `iso_code`

> String: Distinct values

> [!WARNING]
> Nambia has the ISO code `NA`. By default, `pandas.read_csv` interprets this as a null. To prevent this, you can use the `na_filter=False` parameter.

The country's [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code or equivalent.

### `iso_alpha3_code`

> String: Distinct values

The country's [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code or equivalent.

### `wikidata_id`

> String: Distinct values

The country's [Wikidata](https://www.wikidata.org/) [QID](https://www.wikidata.org/wiki/Wikidata:Identifiers).

### `is_protected`

> Boolean: `True` or `False`

Whether the country appears in Wikimedia's [country protection list](https://wikitech.wikimedia.org/wiki/Country_protection_list) indicating that statistics for the country should not be shared publicly.

### `maxmind_continent`

> String: `Africa`, `Antarctica`, `Asia`, `Europe`, `Northern America`, `Oceania`, or `South America`

The country's continent according to the [MaxMind](https://en.wikipedia.org/wiki/MaxMind) geolocation databases.

### `un_continent`

> String: `Africa`, `Antarctica`, `Asia`, `Europe`, `Latin America and the Caribbean`, `Northern America`, or `Oceania`

The country's continent according to the [United Nations](https://en.wikipedia.org/wiki/United_Nations).

### `un_subcontinent`

> String: `Antarctica`, `Australia and New Zealand`, `Caribbean`, `Central America`, `Central Asia`, `Eastern Africa`, `Eastern Asia`, `Eastern Europe`, `Melanesia`, `Micronesia`, `Middle Africa`, `Northern Africa`, `Northern America`, `Northern Europe`, `Polynesia`, `South America`, `South-eastern Asia`, `Southern Africa`, `Southern Asia`, `Southern Europe`, `Western Africa`, `Western Asia`, or `Western Europe`

The country's subcontinent according to the [United Nations](https://en.wikipedia.org/wiki/United_Nations).

### `un_m49_code`

> String: Distinct values

> [!NOTE]
> Includes null values

The country's [M49 Area Code](https://en.wikipedia.org/wiki/UN_M49) from the [United Nations](https://en.wikipedia.org/wiki/United_Nations).

### `wikimedia_region`

> String: `Central & Eastern Europe & Central Asia`, `East, Southeast Asia, & Pacific`, `Latin America & Caribbean`, `Middle East & North Africa`, `North America`, `Northern & Western Europe`, `South Asia`, or `Sub-Saharan Africa`

> [!NOTE]
> Includes null values

The country's region according to the [Wikimedia Foundation](https://en.wikipedia.org/wiki/Wikimedia_Foundation).

### `grant_committee_region`

> String: `Central & Eastern Europe & Central Asia`, `East, Southeast Asia, & Pacific`, `Latin America & Caribbean`, `Middle East & Africa`, `North America`, `Northern & Western Europe`, or `South Asia`

> [!NOTE]
> Includes null values

The country's classification in regards to regional Grantmaking committees.

### `form_990_region`

> String: `Antarctica`, `Central America and the Caribbean`, `East Asia and the Pacific`, `Europe`, `Middle East and North Africa`, `North America`, `Russia and Neighboring States`, `South America`, `South Asia`, `Sub-Saharan Africa`, or `United States`

> [!NOTE]
> Includes null values

### `economic_region`

> String: `Global North` or `Global South`

The country's classification based on [Global North and Global South](https://en.wikipedia.org/wiki/Global_North_and_Global_South).

### `emerging_classification`

> String: `Developed`, `Emerging`, or `Least Developed`

> [!NOTE]
> Includes null values

The country's emerging classification according to the [IMF](https://en.wikipedia.org/wiki/International_Monetary_Fund) and the [United Nations](https://en.wikipedia.org/wiki/United_Nations).

### `is_eu`

> Boolean: `True` or `False`

Whether the country appears in this [list of countries](https://european-union.europa.eu/principles-countries-history/country-profiles_en) or in this [list of special territories](https://en.wikipedia.org/wiki/Special_territories_of_members_of_the_European_Economic_Area), indicating that it belongs to the [European Union](https://en.wikipedia.org/wiki/European_Union).

### `is_un_member`

> Boolean: `True` or `False`

Whether the country is a member of the [United Nations](https://en.wikipedia.org/wiki/United_Nations).

### `is_un_data_entity`

> Boolean: `True` or `False`

Whether the [United Nations](https://en.wikipedia.org/wiki/United_Nations) has data on the country.

### `is_imf_data_entity`

> Boolean: `True` or `False`

Whether the [IMF](https://en.wikipedia.org/wiki/International_Monetary_Fund) has data on the country.

### `is_world_bank_data_entity`

> Boolean: `True` or `False`

Whether the [World Bank](https://en.wikipedia.org/wiki/World_Bank) has data on the country.

### `is_penn_world_table_data_entity`

> Boolean: `True` or `False`

Whether [Penn World Table](https://en.wikipedia.org/wiki/Penn_World_Table) has data on the country.

### `market_research_classification`

> String: `Build`, `Create`, `Expand`, or `Protect`

> [!NOTE]
> Includes null values

The country's market research classification according to the [Wikimedia Foundation](https://en.wikipedia.org/wiki/Wikimedia_Foundation).
