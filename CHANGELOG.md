# Changelog


## 2024-02-08
- Bump dependency to get the security fix for the reported CVE

## 2024-02-14
- Correct the timestamp format to use ISO 8601 for consistency

## 2024-02-20
- Implement request ID propagation for better tracing across services

## 2024-02-20
- Support config reload without restart via SIGHUP or file watch

## 2024-02-23
- Add proper error handling for invalid config so the app doesn't crash on startup

## 2024-02-29
- Handle the redirect response and follow it to get the final resource

## 2024-02-29
- Remove hardcoded credentials and move to env-based configuration

## 2024-03-03
- Update the API docs with the new query parameters and examples

## 2024-03-12
- Update the example config with all available options and comments

## 2024-03-15
- Correct the default value for the feature flag in production

## 2024-03-15
- Adjust the pool size to match the actual concurrency we need

## 2024-03-18
- Clean up the commented-out code that was left from debugging

## 2024-03-18
- Clean up unused imports and fix formatting to match the project style guide

## 2024-03-18
- Fix issue where empty input was not validated before passing to the parser

## 2024-03-18
- Add a comment explaining why we disable the linter on this line

## 2024-03-30
- Implement a simple metrics endpoint for Prometheus scraping

## 2024-04-05
- Remove the unused parameter that was left from an old refactor

## 2024-04-08
- Improve error message when the required env var is not set

## 2024-04-08
- Fix bug where the parser would hang on malformed input

## 2024-04-11
- Bump the version and tag the release in the repo

## 2024-04-20
- Fix the encoding issue when reading config files with non-ASCII

## 2024-04-23
- Add a small delay between retries to avoid thundering herd

## 2024-04-26
- Refactor utils to use a single source of truth for default values

## 2024-04-29
- Adjust log level for noisy messages that were filling the logs

## 2024-05-08
- Improve performance by caching the result of the expensive lookup
