# Serving

We serve our predictions in two ways:

- Providing an endpoint to the model binary to generate scores given an input node ID and predicate name.
- Retrieving pre-computed scores from the ```predictions/``` directory that are mapped to human-readable string names for validation by SMEs.