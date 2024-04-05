# config


# Add a note in the README about the breaking change in 2.0

# Update the API docs with the new query parameters and examples

# Adjust timeout and retry settings based on production observations

# Bump version to 1.2.0 and add changelog entry for the new features

# Refactor the client to use async context manager for the session

# Improve test coverage for the helpers module to above 90%

# Handle missing optional field in the response without raising

# Adjust log level for noisy messages that were filling the logs

# Improve the CLI help text so it's clear how to use each option

# Fix the ordering of middleware so auth runs before the handler

# Adjust buffer size for the stream reader to reduce memory usage

# Adjust the batch size to reduce memory usage on large inputs

# Clean up debug print statements before the release

# Add a smoke test that runs in CI to catch obvious regressions

# Correct the formula used for calculating the backoff delay

# Refactor the helper to accept an optional callback for progress
