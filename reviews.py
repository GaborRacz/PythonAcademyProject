class Review(object):
    def __init__(self):
        self.submission = False
        self.review_request1 = False
        self.review_request2 = False
        self.review_response1 = False
        self.review_response2 = False
        self.evaluation = False

    def set_submission(self, message):
        if self.submission is self.review_request1 is self.review_request2 is self.review_response1 is self.review_response2 is self.evaluation is False:
            self.submission = True
        else:
            raise ValueError(message)

    def set_review_request_1(self, message):
        if self.submission is True and self.review_request1 is self.review_response1 is self.review_response2 is self.evaluation is False:
            self.review_request1 = True
        else:
            raise ValueError(message)

    def set_review_request_2(self, message):
        if self.submission is True and self.review_request2 is self.review_response1 is self.review_response2 is self.evaluation is False:
            self.review_request2 = True
        else:
            raise ValueError(message)

    def set_review_response_1(self, message):
        if self.submission is self.review_request1 is True and self.review_response1 is self.evaluation is False:
            self.review_response1 = True
        else:
            raise ValueError(message)

    def set_review_response_2(self, message):
        if self.submission is self.review_request2 is True and self.review_response2 is self.evaluation is False:
            self.review_response2 = True
        else:
            raise ValueError(message)

    def set_evaluation_result(self, message):
        if self.evaluation is False and self.submission is self.review_request1 is self.review_request2 is self.review_response1 is self.review_response2 is True:
            self.evaluation = True
        else:
            raise ValueError(message)

class ReviewManager(object):
    def __init__(self, review_location):
        self.review_location = review_location
