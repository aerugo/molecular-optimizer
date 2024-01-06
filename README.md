# Model Card

## Model Description

### Input

The input to this model consists of eight continuous variables representing molecular descriptors (x1 to x8) of a compound.
Data from https://archive.ics.uci.edu/dataset/505/qsar+aquatic+toxicity

### Output

The output is a single continuous variable (y), representing the aquatic toxicity effect of the compound as LC50 [-LOG(mol/L)]. 

## Model Architecture

The model architecture is based on the Trust Region Bayesian Optimization (TuRBO) algorithm, which is a distinct advancement in the field of Bayesian optimization. TuRBO, originally proposed by Eriksson et al., is designed to efficiently optimize functions with many local optima by adaptively shrinking and moving the search region to find the global optimum.

While TuRBO itself was not developed by the Optuna team, the Optuna Developers adapted it in their submission for the NeurIPS 2020 competition, demonstrating its effectiveness and versatility. Their implementation provided a robust, concise codebase, making it an appealing foundation for further adaptation and application to specific problems like predicting aquatic toxicity.

The specific modifications made to adapt the Optuna Developers' TuRBO implementation to this problem include:

* Introduction of Random Seed in __init__ Method: To ensure the reproducibility of results, a random seed initialization parameter was added. This feature is crucial for scientific experiments where repeatability is a must.
* Modification in Handling Real Spaces in the init_grid Method: The original TuRBO algorithm and its subsequent adaptations typically include a grid search component, which is crucial for efficiently exploring the function space. However, for continuous function spaces, this can be challenging. In this implementation, the grid search was enhanced for real spaces by creating a grid with ten steps between the lower and upper bounds of each variable. This change allows for a more thorough and systematic exploration of the search space.
* Removal of the from bayesmark.experiment import experiment_main: References to deprecated libraries were removed to streamline the code and ensure its operability without relying on outdated or unsupported modules. This modification doesn't affect the algorithm's core functionality but rather ensures that the code remains clean and maintainable.

## Performance

The performance was evaluated by the rank and mean of the maximum y value found across 10 runs for several iteration cycle sizes (15, 30, 45, 60, 75, 90). To test the model, for each suggested query point, the algorithm identifies the closest known point from a pre-determined set of experimental results. The model's performance is judged based on the mean of the maximum y values of these closest known points across the 10 tests for each iteration cycle. This approach provides insight into the model's ability to converge towards the most promising chemical compounds (i.e., those with the lowest toxicity) within the given chemical space. 

## Limitations

- **Data-Driven:** The model's performance is heavily reliant on the underlying data. If the data is not representative or is biased, the model may not generalize well to other chemical compounds.
- **Black-Box Nature:** Bayesian optimization is somewhat of a black-box optimizer, making it difficult to understand why certain suggestions are made.
- **Computational Intensity:** The model may require significant computational resources, particularly for larger iteration cycles or more complex chemical spaces.

## Trade-offs

- **Accuracy vs. Speed:** Increasing the number of iterations tends to increase the accuracy of the model but also significantly increases computational time and resources.
- **Exploration vs. Exploitation:** The model must balance between exploring new areas of the chemical space and exploiting the areas known to yield good results.

## References and Citations

* **TuRBO Algorithm:** Eriksson, D., Pearce, M., Gardner, J.R., Turner, R.D., & Poloczek, M. (2019). Scalable Global Optimization via Local Bayesian Optimization. Advances in Neural Information Processing Systems.
* **Optuna Implementation:** The NeurIPS 2020 competition submission by Optuna Developers provided a robust, compact codebase. This implementation of the TuRBO algorithm was adapted for the specific task of modeling aquatic toxicity.
