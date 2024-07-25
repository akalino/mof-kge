# Predictions

For this task, we make link inferences at the predicate level. Via sampling of the graph, we identify triples that are not 
contained in the original graph; these serve as candidates for missing links.
This sampling procedure is done via the tail entity type, i.e. for a head entity such as ```temperature``` with numeric type, 
it does not make sense to use the ```has_publication``` predicate for scoring.