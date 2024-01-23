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

Whether the country appears in Wikimedia's [country and territory protection list](https://foundation.wikimedia.org/wiki/Legal:Country_and_Territory_Protection_List) indicating that statistics for the country should only be shared using differentially-private data publication techniques.

### `data_risk_score`

> Float: `0-100` or `None`

A real-valued data risk score, derived from country and territory scores published annually by Freedom House and Reporters Without Borders. 0 is least risky, 100 is most risky. Countries and territories without a score have a null value.

### `data_risk_classification`

> String: `Lower risk`, `Medium risk`, `Higher risk`, or `Not published`

A risk classification for each country/territory, which corresponds to the data risk score. 0 ≤ score < 60 --> lower risk; 60 ≤ score < 67.5 --> medium risk; 67.5 ≤ score < 75 --> higher risk, 75 ≤ score --> not published.

### `maxmind_continent`

> String: `Africa`, `Antarctica`, `Asia`, `Europe`, `Northern America`, `Oceania`, or `South America`

The country's continent according to the [MaxMind](https://en.wikipedia.org/wiki/MaxMind) geolocation databases.

### `un_continent`

> String: `Africa`, `Antarctica`, `Asia`, `Europe`, `Latin America and the Caribbean`, `Northern America`, or `Oceania`

The country's continent according to [United Nations geoscheme](https://en.wikipedia.org/wiki/United_Nations_geoscheme).

### `un_subcontinent`

> String: `Antarctica`, `Australia and New Zealand`, `Caribbean`, `Central America`, `Central Asia`, `Eastern Africa`, `Eastern Asia`, `Eastern Europe`, `Melanesia`, `Micronesia`, `Middle Africa`, `Northern Africa`, `Northern America`, `Northern Europe`, `Polynesia`, `South America`, `South-eastern Asia`, `Southern Africa`, `Southern Asia`, `Southern Europe`, `Western Africa`, `Western Asia`, or `Western Europe`

The country's subcontinent according to [United Nations geoscheme](https://en.wikipedia.org/wiki/United_Nations_geoscheme).

### `un_m49_code`

> Integer: Distinct values

> [!NOTE]
> Includes null values

The country's [M49 code](https://en.wikipedia.org/wiki/UN_M49) defined by the United Nations.

### `wikimedia_region`

> String: `Central & Eastern Europe & Central Asia`, `East, Southeast Asia, & Pacific`, `Latin America & Caribbean`, `Middle East & North Africa`, `North America`, `Northern & Western Europe`, `South Asia`, or `Sub-Saharan Africa`

> [!NOTE]
> Includes null values

The country's region according to a classification developed by the Wikimedia Foundation in 2022. For more details, see [meta:Wikimedia regions](https://meta.wikimedia.org/wiki/Wikimedia_regions).

### `grant_committee_region`

> String: `Central & Eastern Europe & Central Asia`, `East, Southeast Asia, & Pacific`, `Latin America & Caribbean`, `Middle East & Africa`, `North America`, `Northern & Western Europe`, or `South Asia`

> [!NOTE]
> Includes null values

The country's region according to the classification used for Wikimedia Foundation grantmaking before July 2023. See [meta:Grants:Regions/Changes to funding regions in 2023-24](https://meta.wikimedia.org/wiki/Wikimedia_regions).

### `form_990_region`

> String: `Antarctica`, `Central America and the Caribbean`, `East Asia and the Pacific`, `Europe`, `Middle East and North Africa`, `North America`, `Russia and Neighboring States`, `South America`, `South Asia`, `Sub-Saharan Africa`, or `United States`

> [!NOTE]
> Includes null values

The country's region according to a classification developed by the US Internal Revenue Service for US non-profit organizations to report their activities outside the US. The classification is used in [Schedule F to Form 990](https://www.irs.gov/instructions/i990sf).

### `economic_region`

> String: `Global North` or `Global South`

The country's classification based on [Global North and Global South](https://en.wikipedia.org/wiki/Global_North_and_Global_South).

### `emerging_classification`

> String: `Developed`, `Emerging`, or `Least Developed`

> [!NOTE]
> Includes null values

The classification of the country's Wikimedia contributor community according to a [system developed in 2014](https://meta.wikimedia.org/wiki/Community_Engagement/Defining_Emerging_Communities) by the Wikimedia Foundation's Grantmaking department.

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

The country's classification according to a [system developed in 2020](https://meta.wikimedia.org/wiki/Communications/Research/Global_market_and_audience_research_(2020)#Additional_insights) by the Wikimedia Foundations's Communications department based on market research.