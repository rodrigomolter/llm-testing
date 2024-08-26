from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

from qwen_test_model import QwenTestModel
from qwen_eval_model import QwenEvalModel


def test_answer_relevancy():

    eval_model = QwenEvalModel()
    test_model = QwenTestModel()
    
    prompt = "What is the capital of France?"

    metric = AnswerRelevancyMetric(
        threshold=0.5,
        model=eval_model,
        include_reason=True
    )
    
    test_case = LLMTestCase(
        input=prompt,
        actual_output=test_model.generate(prompt)
    )
    assert_test(test_case, [metric])