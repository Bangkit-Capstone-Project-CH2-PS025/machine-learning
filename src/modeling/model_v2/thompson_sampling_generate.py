from thompson_sampling.bernoulli import BernoulliExperiment
from thompson_sampling.priors import BetaPrior

class ThompsonSamplingGenerate:
    def __init__(self, arms=2):
        self.experiment = BernoulliExperiment(arms=arms)
        self.priors = BetaPrior()

    def add_keywords(self, keywords, expected_keywords):
        for keyword in keywords:
            self.priors.add_one(mean=0.5, variance=0.2, effective_size=5, label=keyword)
        for keyword in expected_keywords:
            self.priors.add_one(mean=0.8, variance=0.05, effective_size=10, label=keyword)
        self.experiment = BernoulliExperiment(priors=self.priors)

    def add_rewards(self, keywords, expected_keywords):
        rewards = []
        for keyword in keywords:
            rewards.append({"label": keyword, "reward": 0})
        for keyword in expected_keywords:
            rewards.append({"label": keyword, "reward": 1})
        self.experiment.add_rewards(rewards)

    def choose_unique_arms(self):
        chosen_arms = set()
        unique_chosen_arms = []
        while len(chosen_arms) < 8:
            chosen_arm = self.experiment.choose_arm()
            if chosen_arm not in chosen_arms:
                chosen_arms.add(chosen_arm)
                unique_chosen_arms.append(chosen_arm)
        return unique_chosen_arms