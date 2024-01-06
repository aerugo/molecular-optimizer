from modified_turbo_optimizer import ModifiedTurboOptimizer

def startModifiedTurboOptimizer(api_config, X_list, y_list):
    turbo_optimizer = ModifiedTurboOptimizer(api_config, random_seed=822) # setting random seed for reproducibility
    turbo_optimizer.batch_size = 1
    turbo_optimizer.create_mask(api_config)
    turbo_optimizer.restart()

    turbo_optimizer.observe(X_list, [-y for y in y_list])

    return turbo_optimizer