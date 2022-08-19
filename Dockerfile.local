FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt  .

RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

ENV OUTPUT_DIR=/tmp

COPY function.py ${LAMBDA_TASK_ROOT}
COPY pkg ${LAMBDA_TASK_ROOT}/pkg

CMD [ "function.lambda_handler" ]