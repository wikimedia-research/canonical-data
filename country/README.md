As of Jan 2023, this dataset contains records for the 249 territories included in [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) as well as two more used by MaxMind, [our geolocation service](https://wikitech.wikimedia.org/wiki/Geolocation):
* Kosovo (code `XK`)
* unknown location (code `--`)

## Fields
### `name`
The country's common English name (generally the title chosen by the English Wikipedia for its article). This means, for example, using "Laos" rather than "Lao People's Democratic Republic" and "Bolivia" rather than "Bolivia (Plurinational State of)".

### `iso_code`
The country's [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code or equivalent.

### `economic_region`
A classification of the country as ["Global North" or "Global South"](https://en.wikipedia.org/wiki/Global_North_and_Global_South).

### `maxmind_continent`
The country's continent according to MaxMind's databases.

### `is_protected`
Whether the country appears in Wikimedia's [country protection list](https://wikitech.wikimedia.org/wiki/Country_protection_list) indicating that statistics for the country should not be shared publicly.
