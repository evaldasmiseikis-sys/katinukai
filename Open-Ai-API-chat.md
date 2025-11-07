### POST /chat/completions

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

**Starting a new project?** We recommend trying [Responses](https://platform.openai.com/docs/api-reference/responses) 
to take advantage of the latest OpenAI platform features. Compare
[Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

---

Creates a model response for the given chat conversation. Learn more in the
[text generation](https://platform.openai.com/docs/guides/text-generation), [vision](https://platform.openai.com/docs/guides/vision),
and [audio](https://platform.openai.com/docs/guides/audio) guides.

Parameter support can differ depending on the model used to generate the
response, particularly for newer reasoning models. Parameters that are only
supported for reasoning models are noted below. For the current state of 
unsupported parameters in reasoning models, 
[refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).


```markdown
### Request Body

**Content-Type:** application/json

- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **top_logprobs** (integer): An integer between 0 and 20 specifying the number of most likely tokens to
return at each token position, each with an associated log probability.
`logprobs` must be set to `true` if this parameter is used.

- **temperature** (number): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.
 (example: 1)
- **top_p** (number): An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.
 (example: 1)
- **user** (string): This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and  to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).
 (example: "user-1234")
- **safety_identifier** (string): A stable identifier used to help detect users of your application that may be violating OpenAI's usage policies.
The IDs should be a string that uniquely identifies each user. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).
 (example: "safety-identifier-1234")
- **prompt_cache_key** (string): Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).
 (example: "prompt-cache-key-1234")
- **service_tier** (string (auto|default|flex|scale|priority)): Specifies the processing type used for serving the request.
  - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
  - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
  - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
  - When not set, the default behavior is 'auto'.

  When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
 ("auto"|"default"|"flex"|"scale"|"priority")
- **messages** (array (object)) (required): A list of messages comprising the conversation so far. Depending on the
[model](https://platform.openai.com/docs/models) you use, different message types (modalities) are
supported, like [text](https://platform.openai.com/docs/guides/text-generation),
[images](https://platform.openai.com/docs/guides/vision), and [audio](https://platform.openai.com/docs/guides/audio).

  Array items:
    - **content** (string) (required): The contents of the developer message.
    - **role** (string (developer)) (required): The role of the messages author, in this case `developer`. ("developer")
    - **name** (string): An optional name for the participant. Provides the model information to differentiate between participants of the same role.
- **model** (string) (required)
- **modalities** (array (string (text|audio))): Output types that you would like the model to generate.
Most models are capable of generating text, which is the default:

`["text"]`

The `gpt-4o-audio-preview` model can also be used to
[generate audio](https://platform.openai.com/docs/guides/audio). To request that this model generate
both text and audio responses, you can use:

`["text", "audio"]`

- **verbosity** (string (low|medium|high)): Constrains the verbosity of the model's response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.
 ("low"|"medium"|"high")
- **reasoning_effort** (string (minimal|low|medium|high)): Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `minimal`, `low`, `medium`, and `high`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
 ("minimal"|"low"|"medium"|"high")
- **max_completion_tokens** (integer): An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

- **frequency_penalty** (number): Number between -2.0 and 2.0. Positive values penalize new tokens based on
their existing frequency in the text so far, decreasing the model's
likelihood to repeat the same line verbatim.

- **presence_penalty** (number): Number between -2.0 and 2.0. Positive values penalize new tokens based on
whether they appear in the text so far, increasing the model's likelihood
to talk about new topics.

- **web_search_options** (object): This tool searches the web for relevant results to use in a response.
Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

  - **user_location** (object): Approximate location parameters for the search.

    - **type** (string (approximate)) (required): The type of location approximation. Always `approximate`.
 ("approximate")
    - **approximate** (object) (required): Approximate location parameters for the search.
      - **country** (string): The two-letter 
[ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user,
e.g. `US`.

      - **region** (string): Free text input for the region of the user, e.g. `California`.

      - **city** (string): Free text input for the city of the user, e.g. `San Francisco`.

      - **timezone** (string): The [IANA timezone](https://timeapi.io/documentation/iana-timezones) 
of the user, e.g. `America/Los_Angeles`.

  - **search_context_size** (string (low|medium|high)): High level guidance for the amount of context window space to use for the 
search. One of `low`, `medium`, or `high`. `medium` is the default.
 ("low"|"medium"|"high")
- **response_format** (object): Default response format. Used to generate text responses.

  - **type** (string (text)) (required): The type of response format being defined. Always `text`. ("text")
- **audio** (object): Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

  - **voice** (string) (required)
  - **format** (string (wav|aac|mp3|flac|opus|pcm16)) (required): Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,
`opus`, or `pcm16`.
 ("wav"|"aac"|"mp3"|"flac"|"opus"|"pcm16")
- **store** (boolean): Whether or not to store the output of this chat completion request for
use in our [model distillation](https://platform.openai.com/docs/guides/distillation) or
[evals](https://platform.openai.com/docs/guides/evals) products.

Supports text and image inputs. Note: image inputs over 8MB will be dropped.

- **stream** (boolean): If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
for more information, along with the [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
guide for more information on how to handle the streaming events.

- **stop** (string) (example: "\n")
- **logit_bias** (object): Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the
tokenizer) to an associated bias value from -100 to 100. Mathematically,
the bias is added to the logits generated by the model prior to sampling.
The exact effect will vary per model, but values between -1 and 1 should
decrease or increase likelihood of selection; values like -100 or 100
should result in a ban or exclusive selection of the relevant token.

- **logprobs** (boolean): Whether to return log probabilities of the output tokens or not. If true,
returns the log probabilities of each output token returned in the
`content` of `message`.

- **max_tokens** (integer): The maximum number of [tokens](/tokenizer) that can be generated in the
chat completion. This value can be used to control
[costs](https://openai.com/api/pricing/) for text generated via API.

This value is now deprecated in favor of `max_completion_tokens`, and is
not compatible with [o-series models](https://platform.openai.com/docs/guides/reasoning).

- **n** (integer): How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs. (example: 1)
- **prediction** (object): Static predicted output content, such as the content of a text file that is
being regenerated.

  - **type** (string (content)) (required): The type of the predicted content you want to provide. This type is
currently always `content`.
 ("content")
  - **content** (string) (required): The content used for a Predicted Output. This is often the
text of a file you are regenerating with minor changes.

- **seed** (integer): This feature is in Beta.
If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

- **stream_options** (object): Options for streaming response. Only set this when you set `stream: true`.

  - **include_usage** (boolean): If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

  - **include_obfuscation** (boolean): When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

- **tools** (array (object)): A list of tools the model may call. You can provide either
[custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools) or
[function tools](https://platform.openai.com/docs/guides/function-calling).

  Array items:
    - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
    - **function** (object) (required)
      - **description** (string): A description of what the function does, used by the model to choose when and how to call the function.
      - **name** (string) (required): The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
      - **parameters** (object): The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.
      - **strict** (boolean): Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).
- **tool_choice** (string (none|auto|required)): `none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools.
 ("none"|"auto"|"required")
- **parallel_tool_calls** (boolean): Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.
- **function_call** (string (none|auto)): `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function.
 ("none"|"auto")
- **functions** (array (object)): Deprecated in favor of `tools`.

A list of functions the model may generate JSON inputs for.

  Array items:
    - **description** (string): A description of what the function does, used by the model to choose when and how to call the function.
    - **name** (string) (required): The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
    - **parameters** (object): The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.

### Responses

#### 200 - OK

**CreateChatCompletionResponse**
- **id** (string) (required): A unique identifier for the chat completion.
- **choices** (array (object)) (required): A list of chat completion choices. Can be more than one if `n` is greater than 1.
  Array items:
    - **finish_reason** (string (stop|length|tool_calls|content_filter|function_call)) (required): The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
 ("stop"|"length"|"tool_calls"|"content_filter"|"function_call")
    - **index** (integer) (required): The index of the choice in the list of choices.
    - **message** (object) (required): A chat completion message generated by the model.
      - **content** (string) (required): The contents of the message.
      - **refusal** (string) (required): The refusal message generated by the model.
      - **tool_calls** (array (object)): The tool calls generated by the model, such as function calls.
        Array items:
          - **id** (string) (required): The ID of the tool call.
          - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
          - **function** (object) (required): The function that the model called.
            - **name** (string) (required): The name of the function to call.
            - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
      - **annotations** (array (object)): Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

        Array items:
          - **type** (string (url_citation)) (required): The type of the URL citation. Always `url_citation`. ("url_citation")
          - **url_citation** (object) (required): A URL citation when using web search.
            - **end_index** (integer) (required): The index of the last character of the URL citation in the message.
            - **start_index** (integer) (required): The index of the first character of the URL citation in the message.
            - **url** (string) (required): The URL of the web resource.
            - **title** (string) (required): The title of the web resource.
      - **role** (string (assistant)) (required): The role of the author of this message. ("assistant")
      - **function_call** (object): Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.
        - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
        - **name** (string) (required): The name of the function to call.
      - **audio** (object): If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

        - **id** (string) (required): Unique identifier for this audio response.
        - **expires_at** (integer) (required): The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

        - **data** (string) (required): Base64 encoded audio bytes generated by the model, in the format
specified in the request.

        - **transcript** (string) (required): Transcript of the audio generated by the model.
    - **logprobs** (object) (required): Log probability information for the choice.
      - **content** (array (object)) (required): A list of message content tokens with log probability information.
        Array items:
          - **token** (string) (required): The token.
          - **logprob** (number) (required): The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.
          - **bytes** (array (integer)) (required): A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.
          - **top_logprobs** (array (object)) (required): List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.
            Array items:
              - **token** (string) (required): The token.
              - **logprob** (number) (required): The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.
              - **bytes** (array (integer)) (required): A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.
      - **refusal** (array (object)) (required): A list of message refusal tokens with log probability information.
        Array items:
- **created** (integer) (required): The Unix timestamp (in seconds) of when the chat completion was created.
- **model** (string) (required): The model used for the chat completion.
- **service_tier** (string (auto|default|flex|scale|priority)): Specifies the processing type used for serving the request.
  - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
  - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
  - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
  - When not set, the default behavior is 'auto'.

  When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
 ("auto"|"default"|"flex"|"scale"|"priority")
- **system_fingerprint** (string): This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

- **object** (string (chat.completion)) (required): The object type, which is always `chat.completion`. ("chat.completion")
- **usage** (object): Usage statistics for the completion request.
  - **completion_tokens** (integer) (required): Number of tokens in the generated completion.
  - **prompt_tokens** (integer) (required): Number of tokens in the prompt.
  - **total_tokens** (integer) (required): Total number of tokens used in the request (prompt + completion).
  - **completion_tokens_details** (object): Breakdown of tokens used in a completion.
    - **accepted_prediction_tokens** (integer): When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

    - **audio_tokens** (integer): Audio input tokens generated by the model.
    - **reasoning_tokens** (integer): Tokens generated by the model for reasoning.
    - **rejected_prediction_tokens** (integer): When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

  - **prompt_tokens_details** (object): Breakdown of tokens used in the prompt.
    - **audio_tokens** (integer): Audio input tokens present in the prompt.
    - **cached_tokens** (integer): Cached tokens present in the prompt.

**CreateChatCompletionStreamResponse**
- **id** (string) (required): A unique identifier for the chat completion. Each chunk has the same ID.
- **choices** (array (object)) (required): A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the
last chunk if you set `stream_options: {"include_usage": true}`.

  Array items:
    - **delta** (object) (required): A chat completion delta generated by streamed model responses.
      - **content** (string): The contents of the chunk message.
      - **function_call** (object): Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.
        - **arguments** (string): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
        - **name** (string): The name of the function to call.
      - **tool_calls** (array (object))
        Array items:
          - **index** (integer) (required)
          - **id** (string): The ID of the tool call.
          - **type** (string (function)): The type of the tool. Currently, only `function` is supported. ("function")
          - **function** (object)
            - **name** (string): The name of the function to call.
            - **arguments** (string): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
      - **role** (string (developer|system|user|assistant|tool)): The role of the author of this message. ("developer"|"system"|"user"|"assistant"|"tool")
      - **refusal** (string): The refusal message generated by the model.
    - **logprobs** (object): Log probability information for the choice.
      - **content** (array (object)) (required): A list of message content tokens with log probability information.
        Array items:
      - **refusal** (array (object)) (required): A list of message refusal tokens with log probability information.
        Array items:
    - **finish_reason** (string (stop|length|tool_calls|content_filter|function_call)) (required): The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
 ("stop"|"length"|"tool_calls"|"content_filter"|"function_call")
    - **index** (integer) (required): The index of the choice in the list of choices.
- **created** (integer) (required): The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.
- **model** (string) (required): The model to generate the completion.
- **service_tier** (string (auto|default|flex|scale|priority)): Specifies the processing type used for serving the request.
  - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
  - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
  - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
  - When not set, the default behavior is 'auto'.

  When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
 ("auto"|"default"|"flex"|"scale"|"priority")
- **system_fingerprint** (string): This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

- **object** (string (chat.completion.chunk)) (required): The object type, which is always `chat.completion.chunk`. ("chat.completion.chunk")
- **usage** (object): Usage statistics for the completion request.

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
  "metadata": "value",
  "top_logprobs": "0",
  "temperature": 1,
  "top_p": 1,
  "user": "user-1234",
  "safety_identifier": "safety-identifier-1234",
  "prompt_cache_key": "prompt-cache-key-1234",
  "service_tier": "auto",
  "messages": [
    {
      "content": "string",
      "role": "developer",
      "name": "string"
    }
  ],
  "model": "string",
  "modalities": [
    "text"
  ],
  "verbosity": "medium",
  "reasoning_effort": "medium",
  "max_completion_tokens": "0",
  "frequency_penalty": "0",
  "presence_penalty": "0",
  "web_search_options": {
    "user_location": {
      "type": "approximate",
      "approximate": {
        "country": "string",
        "region": "string",
        "city": "string",
        "timezone": "string"
      }
    },
    "search_context_size": "medium"
  },
  "response_format": {
    "type": "text"
  },
  "audio": {
    "voice": "string",
    "format": "wav"
  },
  "store": "false",
  "stream": "false",
  "stop": "\n",
  "logit_bias": "null",
  "logprobs": "false",
  "max_tokens": "0",
  "n": 1,
  "prediction": {
    "type": "content",
    "content": "string"
  },
  "seed": "0",
  "stream_options": {
    "include_usage": "true",
    "include_obfuscation": "true"
  },
  "tools": [
    {
      "type": "function",
      "function": {
        "description": "string",
        "name": "string",
        "parameters": "value",
        "strict": "false"
      }
    }
  ],
  "tool_choice": "none",
  "parallel_tool_calls": "true",
  "function_call": "none",
  "functions": [
    {
      "description": "string",
      "name": "string",
      "parameters": "value"
    }
  ]
}'
```

```

--------------------------------

### GET /assistants

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of assistants.

```markdown
### Parameters

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **before** (string, query, optional): A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.


### Responses

#### 200 - OK

**ListAssistantsResponse**
- **object** (string) (required) (example: "list")
- **data** (array (object)) (required)
  Array items:
    - **id** (string) (required): The identifier, which can be referenced in API endpoints.
    - **object** (string (assistant)) (required): The object type, which is always `assistant`. ("assistant")
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the assistant was created.
    - **name** (string) (required): The name of the assistant. The maximum length is 256 characters.

    - **description** (string) (required): The description of the assistant. The maximum length is 512 characters.

    - **model** (string) (required): ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

    - **instructions** (string) (required): The system instructions that the assistant uses. The maximum length is 256,000 characters.

    - **tools** (array (object)) (required): A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

      Array items:
        - **type** (string (code_interpreter)) (required): The type of tool being defined: `code_interpreter` ("code_interpreter")
    - **tool_resources** (object): A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

      - **code_interpreter** (object)
        - **file_ids** (array (string)): A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

      - **file_search** (object)
        - **vector_store_ids** (array (string)): The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

    - **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

    - **temperature** (number): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
 (example: 1)
    - **top_p** (number): An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.
 (example: 1)
    - **response_format** (string (auto)): `auto` is the default value
 ("auto")
- **first_id** (string) (required) (example: "asst_abc123")
- **last_id** (string) (required) (example: "asst_abc456")
- **has_more** (boolean) (required) (example: false)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/assistants?limit=20&order=desc&after=string&before=string"
```

```

--------------------------------

### Schema: FineTuneReinforcementRequestInput

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Per-line training example for reinforcement fine-tuning. Note that `messages` and `tools` are the only reserved keywords.
Any other arbitrary key-value data can be included on training datapoints and will be available to reference during grading under the `{{ item.XXX }}` template variable.
Input messages may contain text or image content only. Audio and file input messages
are not currently supported for fine-tuning.


```markdown
## Schema: FineTuneReinforcementRequestInput

Per-line training example for reinforcement fine-tuning. Note that `messages` and `tools` are the only reserved keywords.
Any other arbitrary key-value data can be included on training datapoints and will be available to reference during grading under the `{{ item.XXX }}` template variable.
Input messages may contain text or image content only. Audio and file input messages
are not currently supported for fine-tuning.


**Type:** object

- **messages** (array (object)) (required)
  Array items:
    - **content** (string) (required): The contents of the developer message.
    - **role** (string (developer)) (required): The role of the messages author, in this case `developer`. ("developer")
    - **name** (string): An optional name for the participant. Provides the model information to differentiate between participants of the same role.
- **tools** (array (object)): A list of tools the model may generate JSON inputs for.
  Array items:
    - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
    - **function** (object) (required)
      - **description** (string): A description of what the function does, used by the model to choose when and how to call the function.
      - **name** (string) (required): The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
      - **parameters** (object): The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.
      - **strict** (boolean): Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

```

--------------------------------

### Schema: FineTunePreferenceRequestInput

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

The per-line training example of a fine-tuning input file for chat models using the dpo method.
Input messages may contain text or image content only. Audio and file input messages
are not currently supported for fine-tuning.


```markdown
## Schema: FineTunePreferenceRequestInput

The per-line training example of a fine-tuning input file for chat models using the dpo method.
Input messages may contain text or image content only. Audio and file input messages
are not currently supported for fine-tuning.


**Type:** object

- **input** (object)
  - **messages** (array (object))
    Array items:
      - **content** (string) (required): The contents of the system message.
      - **role** (string (system)) (required): The role of the messages author, in this case `system`. ("system")
      - **name** (string): An optional name for the participant. Provides the model information to differentiate between participants of the same role.
  - **tools** (array (object)): A list of tools the model may generate JSON inputs for.
    Array items:
      - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
      - **function** (object) (required)
        - **description** (string): A description of what the function does, used by the model to choose when and how to call the function.
        - **name** (string) (required): The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
        - **parameters** (object): The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.
        - **strict** (boolean): Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).
  - **parallel_tool_calls** (boolean): Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.
- **preferred_output** (array (object)): The preferred completion message for the output.
  Array items:
    - **content** (string): The contents of the assistant message.
    - **refusal** (string): The refusal message by the assistant.
    - **role** (string (assistant)) (required): The role of the messages author, in this case `assistant`. ("assistant")
    - **name** (string): An optional name for the participant. Provides the model information to differentiate between participants of the same role.
    - **audio** (object): Data about a previous audio response from the model.
[Learn more](https://platform.openai.com/docs/guides/audio).

      - **id** (string) (required): Unique identifier for a previous audio response from the model.

    - **tool_calls** (array (object)): The tool calls generated by the model, such as function calls.
      Array items:
        - **id** (string) (required): The ID of the tool call.
        - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
        - **function** (object) (required): The function that the model called.
          - **name** (string) (required): The name of the function to call.
          - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
    - **function_call** (object): Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.
      - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
      - **name** (string) (required): The name of the function to call.
- **non_preferred_output** (array (object)): The non-preferred completion message for the output.
  Array items:

```

--------------------------------

### GET /containers

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List Containers

```markdown
### Parameters

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.


### Responses

#### 200 - Success

**ContainerListResource**
- **object** (unknown) (required): The type of object returned, must be 'list'.
- **data** (array (object)) (required): A list of containers.
  Array items:
    - **id** (string) (required): Unique identifier for the container.
    - **object** (string) (required): The type of this object.
    - **name** (string) (required): Name of the container.
    - **created_at** (integer) (required): Unix timestamp (in seconds) when the container was created.
    - **status** (string) (required): Status of the container (e.g., active, deleted).
    - **expires_after** (object): The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

      - **anchor** (string (last_active_at)): The reference point for the expiration. ("last_active_at")
      - **minutes** (integer): The number of minutes after the anchor before the container expires.
- **first_id** (string) (required): The ID of the first container in the list.
- **last_id** (string) (required): The ID of the last container in the list.
- **has_more** (boolean) (required): Whether there are more containers available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/containers?limit=20&order=desc&after=string"
```

```

--------------------------------

### GET /evals

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List evaluations for a project.


```markdown
### Parameters

- **after** (string, query, optional): Identifier for the last eval from the previous pagination request.
- **limit** (integer, query, optional): Number of evals to retrieve.
- **order** (string (asc|desc), query, optional): Sort order for evals by timestamp. Use `asc` for ascending order or `desc` for descending order.
- **order_by** (string (created_at|updated_at), query, optional): Evals can be ordered by creation time or last updated time. Use
`created_at` for creation time or `updated_at` for last updated time.


### Responses

#### 200 - A list of evals

**EvalList**
- **object** (string (list)) (required): The type of this object. It is always set to "list".
 ("list")
- **data** (array (object)) (required): An array of eval objects.

  Array items:
    - **object** (string (eval)) (required): The object type. ("eval")
    - **id** (string) (required): Unique identifier for the evaluation.
    - **name** (string) (required): The name of the evaluation. (example: "Chatbot effectiveness Evaluation")
    - **data_source_config** (object) (required): A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:
- Used to define your testing criteria and
- What data is required when creating a run

      - **type** (string (custom)) (required): The type of data source. Always `custom`. ("custom")
      - **schema** (object) (required): The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

    - **testing_criteria** (array (object)) (required): A list of testing criteria.
      Array items:
        - **type** (string (label_model)) (required): The object type, which is always `label_model`. ("label_model")
        - **name** (string) (required): The name of the grader.
        - **model** (string) (required): The model to use for the evaluation. Must support structured outputs.
        - **input** (array (object)) (required)
          Array items:
            - **role** (string (user|assistant|system|developer)) (required): The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.
 ("user"|"assistant"|"system"|"developer")
            - **content** (string) (required): A text input to the model.

            - **type** (string (message)): The type of the message input. Always `message`.
 ("message")
        - **labels** (array (string)) (required): The labels to assign to each item in the evaluation.
        - **passing_labels** (array (string)) (required): The labels that indicate a passing result. Must be a subset of labels.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the eval was created.
    - **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **first_id** (string) (required): The identifier of the first eval in the data array.
- **last_id** (string) (required): The identifier of the last eval in the data array.
- **has_more** (boolean) (required): Indicates whether there are more evals available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/evals?after=string&limit=20&order=asc&order_by=created_at"
```

```

--------------------------------

### GET /organization/projects

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of projects.

```markdown
### Parameters

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **include_archived** (boolean, query, optional): If `true` returns all projects including those that have been `archived`. Archived projects are not included by default.

### Responses

#### 200 - Projects listed successfully.

**ProjectListResponse**
- **object** (string (list)) (required) ("list")
- **data** (array (object)) (required)
  Array items:
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **object** (string (organization.project)) (required): The object type, which is always `organization.project` ("organization.project")
    - **name** (string) (required): The name of the project. This appears in reporting.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) of when the project was created.
    - **archived_at** (integer): The Unix timestamp (in seconds) of when the project was archived or `null`.
    - **status** (string (active|archived)) (required): `active` or `archived` ("active"|"archived")
- **first_id** (string) (required)
- **last_id** (string) (required)
- **has_more** (boolean) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/projects?limit=20&after=string&include_archived=false"
```

```

--------------------------------

### GET /files

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of files.

```markdown
### Parameters

- **purpose** (string, query, optional): Only return files with the given purpose.
- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.


### Responses

#### 200 - OK

**ListFilesResponse**
- **object** (string) (required) (example: "list")
- **data** (array (object)) (required)
- **first_id** (string) (required) (example: "file-abc123")
- **last_id** (string) (required) (example: "file-abc456")
- **has_more** (boolean) (required) (example: false)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/files?purpose=string&limit=10000&order=desc&after=string"
```

```

--------------------------------

### GET /organization/usage/completions

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get completions usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **user_ids** (array (string), query, optional): Return only usage for these users.
- **api_key_ids** (array (string), query, optional): Return only usage for these API keys.
- **models** (array (string), query, optional): Return only usage for these models.
- **batch** (boolean, query, optional): If `true`, return batch jobs only. If `false`, return non-batch jobs only. By default, return both.

- **group_by** (array (string (project_id|user_id|api_key_id|model|batch|service_tier)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `batch`, `service_tier` or any combination of them.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/completions?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&user_ids=item1,item2&api_key_ids=item1,item2&models=item1,item2&batch=true&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### GET /videos

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List videos

```markdown
### Parameters

- **limit** (integer, query, optional): Number of items to retrieve
- **order** (OrderEnum, query, optional): Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.
- **after** (string, query, optional): Identifier for the last item from the previous pagination request

### Responses

#### 200 - Success

**VideoListResource**
- **object** (unknown) (required): The type of object returned, must be `list`.
- **data** (array (object)) (required): A list of items
  Array items:
    - **id** (string) (required): Unique identifier for the video job.
    - **object** (string (video)) (required): The object type, which is always `video`. ("video")
    - **model** (string (sora-2|sora-2-pro)) (required) ("sora-2"|"sora-2-pro")
    - **status** (string (queued|in_progress|completed|failed)) (required) ("queued"|"in_progress"|"completed"|"failed")
    - **progress** (integer) (required): Approximate completion percentage for the generation task.
    - **created_at** (integer) (required): Unix timestamp (seconds) for when the job was created.
    - **completed_at** (integer) (required): Unix timestamp (seconds) for when the job completed, if finished.
    - **expires_at** (integer) (required): Unix timestamp (seconds) for when the downloadable assets expire, if set.
    - **size** (string (720x1280|1280x720|1024x1792|1792x1024)) (required) ("720x1280"|"1280x720"|"1024x1792"|"1792x1024")
    - **seconds** (string (4|8|12)) (required) ("4"|"8"|"12")
    - **remixed_from_video_id** (string) (required): Identifier of the source video if this video is a remix.
    - **error** (object) (required)
      - **code** (string) (required)
      - **message** (string) (required)
- **first_id** (string) (required): The ID of the first item in the list.
- **last_id** (string) (required): The ID of the last item in the list.
- **has_more** (boolean) (required): Whether there are more items available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/videos?limit=0&order=value&after=string"
```

```

--------------------------------

### GET /models

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Lists the currently available models, and provides basic information about each one such as the owner and availability.

```markdown
### Responses

#### 200 - OK

**ListModelsResponse**
- **object** (string (list)) (required) ("list")
- **data** (array (object)) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/models"
```

```

--------------------------------

### Schema: FunctionParameters

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.

```markdown
## Schema: FunctionParameters

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.

**Type:** object


```

--------------------------------

### Schema: RealtimeBetaServerEventResponseMCPCallInProgress

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returned when an MCP tool call has started and is in progress.

```markdown
## Schema: RealtimeBetaServerEventResponseMCPCallInProgress

Returned when an MCP tool call has started and is in progress.

**Type:** object

- **event_id** (string) (required): The unique ID of the server event.
- **type** (unknown) (required): The event type, must be `response.mcp_call.in_progress`.
- **output_index** (integer) (required): The index of the output item in the response.
- **item_id** (string) (required): The ID of the MCP tool call item.

```

--------------------------------

### GET /organization/costs

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get costs details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1d), query, optional): Width of each time bucket in response. Currently only `1d` is supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only costs for these projects.
- **group_by** (array (string (project_id|line_item)), query, optional): Group the costs by the specified fields. Support fields include `project_id`, `line_item` and any combination of them.
- **limit** (integer, query, optional): A limit on the number of buckets to be returned. Limit can range between 1 and 180, and the default is 7.

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Costs data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/costs?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&group_by=item1,item2&limit=7&page=string"
```

```

--------------------------------

### Schema: FineTuneChatRequestInput

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

The per-line training example of a fine-tuning input file for chat models using the supervised method.
Input messages may contain text or image content only. Audio and file input messages
are not currently supported for fine-tuning.


```markdown
## Schema: FineTuneChatRequestInput

The per-line training example of a fine-tuning input file for chat models using the supervised method.
Input messages may contain text or image content only. Audio and file input messages
are not currently supported for fine-tuning.


**Type:** object

- **messages** (array (object))
  Array items:
    - **content** (string) (required): The contents of the system message.
    - **role** (string (system)) (required): The role of the messages author, in this case `system`. ("system")
    - **name** (string): An optional name for the participant. Provides the model information to differentiate between participants of the same role.
- **tools** (array (object)): A list of tools the model may generate JSON inputs for.
  Array items:
    - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
    - **function** (object) (required)
      - **description** (string): A description of what the function does, used by the model to choose when and how to call the function.
      - **name** (string) (required): The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
      - **parameters** (object): The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.
      - **strict** (boolean): Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).
- **parallel_tool_calls** (boolean): Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.
- **functions** (array (object)): A list of functions the model may generate JSON inputs for.
  Array items:
    - **description** (string): A description of what the function does, used by the model to choose when and how to call the function.
    - **name** (string) (required): The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
    - **parameters** (object): The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. 

Omitting `parameters` defines a function with an empty parameter list.

```

--------------------------------

### Schema: RealtimeServerEventConversationItemRetrieved

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returned when a conversation item is retrieved with `conversation.item.retrieve`. This is provided as a way to fetch the server's representation of an item, for example to get access to the post-processed audio data after noise cancellation and VAD. It includes the full content of the Item, including audio data.


```markdown
## Schema: RealtimeServerEventConversationItemRetrieved

Returned when a conversation item is retrieved with `conversation.item.retrieve`. This is provided as a way to fetch the server's representation of an item, for example to get access to the post-processed audio data after noise cancellation and VAD. It includes the full content of the Item, including audio data.


**Type:** object

- **event_id** (string) (required): The unique ID of the server event.
- **type** (unknown) (required): The event type, must be `conversation.item.retrieved`.
- **item** (object) (required): A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation's behavior, use instructions, but for smaller updates (e.g. "the user is now asking about a different topic"), use system messages.
  - **id** (string): The unique ID of the item. This may be provided by the client or generated by the server.
  - **object** (string (realtime.item)): Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item. ("realtime.item")
  - **type** (string (message)) (required): The type of the item. Always `message`. ("message")
  - **status** (string (completed|incomplete|in_progress)): The status of the item. Has no effect on the conversation. ("completed"|"incomplete"|"in_progress")
  - **role** (string (system)) (required): The role of the message sender. Always `system`. ("system")
  - **content** (array (object)) (required): The content of the message.
    Array items:
      - **type** (string (input_text)): The content type. Always `input_text` for system messages. ("input_text")
      - **text** (string): The text content.

```

--------------------------------

### GET /organization/certificates/{certificate_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get a certificate that has been uploaded to the organization.

You can get a certificate regardless of whether it is active or not.


```markdown
### Parameters

- **certificate_id** (string, path, required): Unique ID of the certificate to retrieve.
- **include** (array (string (content)), query, optional): A list of additional fields to include in the response. Currently the only supported value is `content` to fetch the PEM content of the certificate.

### Responses

#### 200 - Certificate retrieved successfully.

**Certificate**
- **object** (string (certificate|organization.certificate|organization.project.certificate)) (required): The object type.

- If creating, updating, or getting a specific certificate, the object type is `certificate`.
- If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
- If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.
 ("certificate"|"organization.certificate"|"organization.project.certificate")
- **id** (string) (required): The identifier, which can be referenced in API endpoints
- **name** (string) (required): The name of the certificate.
- **created_at** (integer) (required): The Unix timestamp (in seconds) of when the certificate was uploaded.
- **certificate_details** (object) (required)
  - **valid_at** (integer): The Unix timestamp (in seconds) of when the certificate becomes valid.
  - **expires_at** (integer): The Unix timestamp (in seconds) of when the certificate expires.
  - **content** (string): The content of the certificate in PEM format.
- **active** (boolean): Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/certificates/{certificate_id}?include=item1,item2"
```

```

--------------------------------

### GET /batches

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List your organization's batches.

```markdown
### Parameters

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.


### Responses

#### 200 - Batch listed successfully.

**ListBatchesResponse**
- **data** (array (object)) (required)
  Array items:
    - **id** (string) (required)
    - **object** (string (batch)) (required): The object type, which is always `batch`. ("batch")
    - **endpoint** (string) (required): The OpenAI API endpoint used by the batch.
    - **model** (string): Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

    - **errors** (object)
      - **object** (string): The object type, which is always `list`.
      - **data** (array (object))
        Array items:
          - **code** (string): An error code identifying the error type.
          - **message** (string): A human-readable message providing more details about the error.
          - **param** (string): The name of the parameter that caused the error, if applicable.
          - **line** (integer): The line number of the input file where the error occurred, if applicable.
    - **input_file_id** (string) (required): The ID of the input file for the batch.
    - **completion_window** (string) (required): The time frame within which the batch should be processed.
    - **status** (string (validating|failed|in_progress|finalizing|completed|expired|cancelling|cancelled)) (required): The current status of the batch. ("validating"|"failed"|"in_progress"|"finalizing"|"completed"|"expired"|"cancelling"|"cancelled")
    - **output_file_id** (string): The ID of the file containing the outputs of successfully executed requests.
    - **error_file_id** (string): The ID of the file containing the outputs of requests with errors.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the batch was created.
    - **in_progress_at** (integer): The Unix timestamp (in seconds) for when the batch started processing.
    - **expires_at** (integer): The Unix timestamp (in seconds) for when the batch will expire.
    - **finalizing_at** (integer): The Unix timestamp (in seconds) for when the batch started finalizing.
    - **completed_at** (integer): The Unix timestamp (in seconds) for when the batch was completed.
    - **failed_at** (integer): The Unix timestamp (in seconds) for when the batch failed.
    - **expired_at** (integer): The Unix timestamp (in seconds) for when the batch expired.
    - **cancelling_at** (integer): The Unix timestamp (in seconds) for when the batch started cancelling.
    - **cancelled_at** (integer): The Unix timestamp (in seconds) for when the batch was cancelled.
    - **request_counts** (object): The request counts for different statuses within the batch.
      - **total** (integer) (required): Total number of requests in the batch.
      - **completed** (integer) (required): Number of requests that have been completed successfully.
      - **failed** (integer) (required): Number of requests that have failed.
    - **usage** (object): Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

      - **input_tokens** (integer) (required): The number of input tokens.
      - **input_tokens_details** (object) (required): A detailed breakdown of the input tokens.
        - **cached_tokens** (integer) (required): The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

      - **output_tokens** (integer) (required): The number of output tokens.
      - **output_tokens_details** (object) (required): A detailed breakdown of the output tokens.
        - **reasoning_tokens** (integer) (required): The number of reasoning tokens.
      - **total_tokens** (integer) (required): The total number of tokens used.
    - **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **first_id** (string) (example: "batch_abc123")
- **last_id** (string) (example: "batch_abc456")
- **has_more** (boolean) (required)
- **object** (string (list)) (required) ("list")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/batches?after=string&limit=20"
```

```

--------------------------------

### Schema: RealtimeServerEventResponseMCPCallInProgress

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returned when an MCP tool call has started and is in progress.

```markdown
## Schema: RealtimeServerEventResponseMCPCallInProgress

Returned when an MCP tool call has started and is in progress.

**Type:** object

- **event_id** (string) (required): The unique ID of the server event.
- **type** (unknown) (required): The event type, must be `response.mcp_call.in_progress`.
- **output_index** (integer) (required): The index of the output item in the response.
- **item_id** (string) (required): The ID of the MCP tool call item.

```

--------------------------------

### GET /conversations/{conversation_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get a conversation

```markdown
### Parameters

- **conversation_id** (string, path, required): The ID of the conversation to retrieve. (example: "conv_123")

### Responses

#### 200 - Success

**ConversationResource**
- **id** (string) (required): The unique ID of the conversation.
- **object** (string (conversation)) (required): The object type, which is always `conversation`. ("conversation")
- **metadata** (unknown) (required): Set of 16 key-value pairs that can be attached to an object. This can be         useful for storing additional information about the object in a structured         format, and querying for objects via API or the dashboard.
        Keys are strings with a maximum length of 64 characters. Values are strings         with a maximum length of 512 characters.
- **created_at** (integer) (required): The time at which the conversation was created, measured in seconds since the Unix epoch.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/conversations/{conversation_id}"
```

```

--------------------------------

### GET /organization/usage/images

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get images usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **sources** (array (string (image.generation|image.edit|image.variation)), query, optional): Return only usages for these sources. Possible values are `image.generation`, `image.edit`, `image.variation` or any combination of them.
- **sizes** (array (string (256x256|512x512|1024x1024|1792x1792|1024x1792)), query, optional): Return only usages for these image sizes. Possible values are `256x256`, `512x512`, `1024x1024`, `1792x1792`, `1024x1792` or any combination of them.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **user_ids** (array (string), query, optional): Return only usage for these users.
- **api_key_ids** (array (string), query, optional): Return only usage for these API keys.
- **models** (array (string), query, optional): Return only usage for these models.
- **group_by** (array (string (project_id|user_id|api_key_id|model|size|source)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `size`, `source` or any combination of them.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/images?start_time=0&end_time=0&bucket_width=1d&sources=item1,item2&sizes=item1,item2&project_ids=item1,item2&user_ids=item1,item2&api_key_ids=item1,item2&models=item1,item2&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### POST /assistants

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create an assistant with a model and instructions.

```markdown
### Request Body

**Content-Type:** application/json

- **model** (string) (required)
- **name** (string): The name of the assistant. The maximum length is 256 characters.

- **description** (string): The description of the assistant. The maximum length is 512 characters.

- **instructions** (string): The system instructions that the assistant uses. The maximum length is 256,000 characters.

- **reasoning_effort** (string (minimal|low|medium|high)): Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `minimal`, `low`, `medium`, and `high`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
 ("minimal"|"low"|"medium"|"high")
- **tools** (array (object)): A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

  Array items:
    - **type** (string (code_interpreter)) (required): The type of tool being defined: `code_interpreter` ("code_interpreter")
- **tool_resources** (object): A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

  - **code_interpreter** (object)
    - **file_ids** (array (string)): A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

  - **file_search** (unknown)
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **temperature** (number): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
 (example: 1)
- **top_p** (number): An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.
 (example: 1)
- **response_format** (string (auto)): `auto` is the default value
 ("auto")

### Responses

#### 200 - OK

**AssistantObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (assistant)) (required): The object type, which is always `assistant`. ("assistant")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the assistant was created.
- **name** (string) (required): The name of the assistant. The maximum length is 256 characters.

- **description** (string) (required): The description of the assistant. The maximum length is 512 characters.

- **model** (string) (required): ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

- **instructions** (string) (required): The system instructions that the assistant uses. The maximum length is 256,000 characters.

- **tools** (array (object)) (required): A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

  Array items:
    - **type** (string (code_interpreter)) (required): The type of tool being defined: `code_interpreter` ("code_interpreter")
- **tool_resources** (object): A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

  - **code_interpreter** (object)
    - **file_ids** (array (string)): A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

  - **file_search** (object)
    - **vector_store_ids** (array (string)): The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **temperature** (number): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
 (example: 1)
- **top_p** (number): An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.
 (example: 1)
- **response_format** (string (auto)): `auto` is the default value
 ("auto")

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/assistants" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "string",
  "name": "string",
  "description": "string",
  "instructions": "string",
  "reasoning_effort": "medium",
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "tool_resources": {
    "code_interpreter": {
      "file_ids": [
        "string"
      ]
    },
    "file_search": "value"
  },
  "metadata": "value",
  "temperature": 1,
  "top_p": 1,
  "response_format": "auto"
}'
```

```

--------------------------------

### GET /organization/usage/moderations

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get moderations usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **user_ids** (array (string), query, optional): Return only usage for these users.
- **api_key_ids** (array (string), query, optional): Return only usage for these API keys.
- **models** (array (string), query, optional): Return only usage for these models.
- **group_by** (array (string (project_id|user_id|api_key_id|model)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/moderations?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&user_ids=item1,item2&api_key_ids=item1,item2&models=item1,item2&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### GET /evals/{eval_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get an evaluation by ID.


```markdown
### Parameters

- **eval_id** (string, path, required): The ID of the evaluation to retrieve.

### Responses

#### 200 - The evaluation

**Eval**
- **object** (string (eval)) (required): The object type. ("eval")
- **id** (string) (required): Unique identifier for the evaluation.
- **name** (string) (required): The name of the evaluation. (example: "Chatbot effectiveness Evaluation")
- **data_source_config** (object) (required): A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:
- Used to define your testing criteria and
- What data is required when creating a run

  - **type** (string (custom)) (required): The type of data source. Always `custom`. ("custom")
  - **schema** (object) (required): The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

- **testing_criteria** (array (object)) (required): A list of testing criteria.
  Array items:
    - **type** (string (label_model)) (required): The object type, which is always `label_model`. ("label_model")
    - **name** (string) (required): The name of the grader.
    - **model** (string) (required): The model to use for the evaluation. Must support structured outputs.
    - **input** (array (object)) (required)
      Array items:
        - **role** (string (user|assistant|system|developer)) (required): The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.
 ("user"|"assistant"|"system"|"developer")
        - **content** (string) (required): A text input to the model.

        - **type** (string (message)): The type of the message input. Always `message`.
 ("message")
    - **labels** (array (string)) (required): The labels to assign to each item in the evaluation.
    - **passing_labels** (array (string)) (required): The labels that indicate a passing result. Must be a subset of labels.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the eval was created.
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/evals/{eval_id}"
```

```

--------------------------------

### Schema: CreateFineTuningJobRequest

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Schema definition for CreateFineTuningJobRequest

```markdown
## Schema: CreateFineTuningJobRequest

Schema definition for CreateFineTuningJobRequest

**Type:** object

- **model** (string) (required)
- **training_file** (string) (required): The ID of an uploaded file that contains training data.

See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

The contents of the file should differ depending on if the model uses the [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input), [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) format, or if the fine-tuning method uses the [preference](https://platform.openai.com/docs/api-reference/fine-tuning/preference-input) format.

See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.
 (example: "file-abc123")
- **hyperparameters** (object): The hyperparameters used for the fine-tuning job.
This value is now deprecated in favor of `method`, and should be passed in under the `method` parameter.

  - **batch_size** (string (auto)) ("auto")
  - **learning_rate_multiplier** (string (auto)) ("auto")
  - **n_epochs** (string (auto)) ("auto")
- **suffix** (string): A string of up to 64 characters that will be added to your fine-tuned model name.

For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.

- **validation_file** (string): The ID of an uploaded file that contains validation data.

If you provide this file, the data is used to generate validation
metrics periodically during fine-tuning. These metrics can be viewed in
the fine-tuning results file.
The same data should not be present in both train and validation files.

Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.
 (example: "file-abc123")
- **integrations** (array (object)): A list of integrations to enable for your fine-tuning job.
  Array items:
    - **type** (string (wandb)) (required) ("wandb")
    - **wandb** (object) (required): The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

      - **project** (string) (required): The name of the project that the new run will be created under.
 (example: "my-wandb-project")
      - **name** (string): A display name to set for the run. If not set, we will use the Job ID as the name.

      - **entity** (string): The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - **tags** (array (string)): A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

- **seed** (integer): The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
If a seed is not specified, one will be generated for you.
 (example: 42)
- **method** (object): The method used for fine-tuning.
  - **type** (string (supervised|dpo|reinforcement)) (required): The type of method. Is either `supervised`, `dpo`, or `reinforcement`. ("supervised"|"dpo"|"reinforcement")
  - **supervised** (object): Configuration for the supervised fine-tuning method.
    - **hyperparameters** (object): The hyperparameters used for the fine-tuning job.
      - **batch_size** (string (auto)) ("auto")
      - **learning_rate_multiplier** (string (auto)) ("auto")
      - **n_epochs** (string (auto)) ("auto")
  - **dpo** (object): Configuration for the DPO fine-tuning method.
    - **hyperparameters** (object): The hyperparameters used for the DPO fine-tuning job.
      - **beta** (string (auto)) ("auto")
      - **batch_size** (string (auto)) ("auto")
      - **learning_rate_multiplier** (string (auto)) ("auto")
      - **n_epochs** (string (auto)) ("auto")
  - **reinforcement** (object): Configuration for the reinforcement fine-tuning method.
    - **grader** (object) (required): A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - **type** (string (string_check)) (required): The object type, which is always `string_check`. ("string_check")
      - **name** (string) (required): The name of the grader.
      - **input** (string) (required): The input text. This may include template strings.
      - **reference** (string) (required): The reference text. This may include template strings.
      - **operation** (string (eq|ne|like|ilike)) (required): The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`. ("eq"|"ne"|"like"|"ilike")
    - **hyperparameters** (object): The hyperparameters used for the reinforcement fine-tuning job.
      - **batch_size** (string (auto)) ("auto")
      - **learning_rate_multiplier** (string (auto)) ("auto")
      - **n_epochs** (string (auto)) ("auto")
      - **reasoning_effort** (string (default|low|medium|high)): Level of reasoning effort.
 ("default"|"low"|"medium"|"high")
      - **compute_multiplier** (string (auto)) ("auto")
      - **eval_interval** (string (auto)) ("auto")
      - **eval_samples** (string (auto)) ("auto")
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


```

--------------------------------

### GET /organization/usage/vector_stores

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get vector stores usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **group_by** (array (string (project_id)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/vector_stores?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### GET /organization/usage/embeddings

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get embeddings usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **user_ids** (array (string), query, optional): Return only usage for these users.
- **api_key_ids** (array (string), query, optional): Return only usage for these API keys.
- **models** (array (string), query, optional): Return only usage for these models.
- **group_by** (array (string (project_id|user_id|api_key_id|model)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/embeddings?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&user_ids=item1,item2&api_key_ids=item1,item2&models=item1,item2&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### POST /files

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Upload a file that can be used across various endpoints. Individual files
can be up to 512 MB, and the size of all files uploaded by one organization
can be up to 1 TB.

- The Assistants API supports files up to 2 million tokens and of specific
  file types. See the [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools) for
  details.
- The Fine-tuning API only supports `.jsonl` files. The input also has
  certain required formats for fine-tuning
  [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input) or
  [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) models.
- The Batch API only supports `.jsonl` files up to 200 MB in size. The input
  also has a specific required
  [format](https://platform.openai.com/docs/api-reference/batch/request-input).

Please [contact us](https://help.openai.com/) if you need to increase these
storage limits.


```markdown
### Request Body

**Content-Type:** multipart/form-data

- **file** (string (binary)) (required): The File object (not file name) to be uploaded.

- **purpose** (string (assistants|batch|fine-tune|vision|user_data|evals)) (required): The intended purpose of the uploaded file. One of: - `assistants`: Used in the Assistants API - `batch`: Used in the Batch API - `fine-tune`: Used for fine-tuning - `vision`: Images used for vision fine-tuning - `user_data`: Flexible file type for any purpose - `evals`: Used for eval data sets
 ("assistants"|"batch"|"fine-tune"|"vision"|"user_data"|"evals")
- **expires_after** (object): The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.
  - **anchor** (string (created_at)) (required): Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. ("created_at")
  - **seconds** (integer) (required): The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Responses

#### 200 - OK

**OpenAIFile**

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/files" \
  -H "Content-Type: application/json" \
  -d '{
  "file": "string",
  "purpose": "assistants",
  "expires_after": {
    "anchor": "created_at",
    "seconds": "0"
  }
}'
```

```

--------------------------------

### GET /organization/usage/audio_speeches

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get audio speeches usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **user_ids** (array (string), query, optional): Return only usage for these users.
- **api_key_ids** (array (string), query, optional): Return only usage for these API keys.
- **models** (array (string), query, optional): Return only usage for these models.
- **group_by** (array (string (project_id|user_id|api_key_id|model)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/audio_speeches?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&user_ids=item1,item2&api_key_ids=item1,item2&models=item1,item2&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### GET /organization/usage/audio_transcriptions

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get audio transcriptions usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **user_ids** (array (string), query, optional): Return only usage for these users.
- **api_key_ids** (array (string), query, optional): Return only usage for these API keys.
- **models** (array (string), query, optional): Return only usage for these models.
- **group_by** (array (string (project_id|user_id|api_key_id|model)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/audio_transcriptions?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&user_ids=item1,item2&api_key_ids=item1,item2&models=item1,item2&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### POST /fine_tuning/alpha/graders/run

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Run a grader.


```markdown
### Request Body

**Content-Type:** application/json

- **grader** (object) (required): A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

  - **type** (string (string_check)) (required): The object type, which is always `string_check`. ("string_check")
  - **name** (string) (required): The name of the grader.
  - **input** (string) (required): The input text. This may include template strings.
  - **reference** (string) (required): The reference text. This may include template strings.
  - **operation** (string (eq|ne|like|ilike)) (required): The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`. ("eq"|"ne"|"like"|"ilike")
- **item** (object): The dataset item provided to the grader. This will be used to populate 
the `item` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details. 

- **model_sample** (string) (required): The model sample to be evaluated. This value will be used to populate 
the `sample` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.
The `output_json` variable will be populated if the model sample is a 
valid JSON string.
 


### Responses

#### 200 - OK

**RunGraderResponse**
- **reward** (number) (required)
- **metadata** (object) (required)
  - **name** (string) (required)
  - **type** (string) (required)
  - **errors** (object) (required)
    - **formula_parse_error** (boolean) (required)
    - **sample_parse_error** (boolean) (required)
    - **truncated_observation_error** (boolean) (required)
    - **unresponsive_reward_error** (boolean) (required)
    - **invalid_variable_error** (boolean) (required)
    - **other_error** (boolean) (required)
    - **python_grader_server_error** (boolean) (required)
    - **python_grader_server_error_type** (string) (required)
    - **python_grader_runtime_error** (boolean) (required)
    - **python_grader_runtime_error_details** (string) (required)
    - **model_grader_server_error** (boolean) (required)
    - **model_grader_refusal_error** (boolean) (required)
    - **model_grader_parse_error** (boolean) (required)
    - **model_grader_server_error_details** (string) (required)
  - **execution_time** (number) (required)
  - **scores** (object) (required)
  - **token_usage** (integer) (required)
  - **sampled_model_name** (string) (required)
- **sub_rewards** (object) (required)
- **model_grader_token_usage_per_model** (object) (required)

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/fine_tuning/alpha/graders/run" \
  -H "Content-Type: application/json" \
  -d '{
  "grader": {
    "type": "string_check",
    "name": "string",
    "input": "string",
    "reference": "string",
    "operation": "eq"
  },
  "item": "value",
  "model_sample": "string"
}'
```

```

--------------------------------

### POST /responses

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Creates a model response. Provide [text](https://platform.openai.com/docs/guides/text) or
[image](https://platform.openai.com/docs/guides/images) inputs to generate [text](https://platform.openai.com/docs/guides/text)
or [JSON](https://platform.openai.com/docs/guides/structured-outputs) outputs. Have the model call
your own [custom code](https://platform.openai.com/docs/guides/function-calling) or use built-in
[tools](https://platform.openai.com/docs/guides/tools) like [web search](https://platform.openai.com/docs/guides/tools-web-search)
or [file search](https://platform.openai.com/docs/guides/tools-file-search) to use your own data
as input for the model's response.


```markdown
### Request Body

**Content-Type:** application/json

- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **top_logprobs** (integer): An integer between 0 and 20 specifying the number of most likely tokens to
return at each token position, each with an associated log probability.

- **temperature** (number): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.
 (example: 1)
- **top_p** (number): An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.
 (example: 1)
- **user** (string): This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and  to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).
 (example: "user-1234")
- **safety_identifier** (string): A stable identifier used to help detect users of your application that may be violating OpenAI's usage policies.
The IDs should be a string that uniquely identifies each user. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).
 (example: "safety-identifier-1234")
- **prompt_cache_key** (string): Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).
 (example: "prompt-cache-key-1234")
- **service_tier** (string (auto|default|flex|scale|priority)): Specifies the processing type used for serving the request.
  - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
  - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
  - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
  - When not set, the default behavior is 'auto'.

  When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
 ("auto"|"default"|"flex"|"scale"|"priority")
- **previous_response_id** (string): The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

- **model** (string)
- **reasoning** (object): **gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

  - **effort** (string (minimal|low|medium|high)): Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `minimal`, `low`, `medium`, and `high`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
 ("minimal"|"low"|"medium"|"high")
  - **summary** (string (auto|concise|detailed)): A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is only supported for `computer-use-preview` models.
 ("auto"|"concise"|"detailed")
  - **generate_summary** (string (auto|concise|detailed)): **Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.
 ("auto"|"concise"|"detailed")
- **background** (boolean): Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

- **max_output_tokens** (integer): An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

- **max_tool_calls** (integer): The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

- **text** (object): Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:
- [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

  - **format** (object): Default response format. Used to generate text responses.

    - **type** (string (text)) (required): The type of response format being defined. Always `text`. ("text")
  - **verbosity** (string (low|medium|high)): Constrains the verbosity of the model's response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.
 ("low"|"medium"|"high")
- **tools** (array (object)): An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

We support the following categories of tools:
- **Built-in tools**: Tools that are provided by OpenAI that extend the
  model's capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
- **MCP Tools**: Integrations with third-party systems via custom MCP servers
  or predefined connectors such as Google Drive and SharePoint. Learn more about
  [MCP Tools](https://platform.openai.com/docs/guides/tools-connectors-mcp).
- **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code with strongly typed arguments
  and outputs. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling). You can also use
  custom tools to call your own code.

  Array items:
    - **type** (string (function)) (required): The type of the function tool. Always `function`. ("function")
    - **name** (string) (required): The name of the function to call.
    - **description** (string): A description of the function. Used by the model to determine whether or not to call the function.
    - **parameters** (object) (required): A JSON schema object describing the parameters of the function.
    - **strict** (boolean) (required): Whether to enforce strict parameter validation. Default `true`.
- **tool_choice** (string (none|auto|required)): Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.
 ("none"|"auto"|"required")
- **prompt** (object): Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

  - **id** (string) (required): The unique identifier of the prompt template to use.
  - **version** (string): Optional version of the prompt template.
  - **variables** (object): Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

- **truncation** (string (auto|disabled)): The truncation strategy to use for the model response.
- `auto`: If the input to this Response exceeds
  the model's context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
- `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.
 ("auto"|"disabled")
- **input** (string): A text input to the model, equivalent to a text input with the
`user` role.

- **include** (array (string (file_search_call.results|web_search_call.results|web_search_call.action.sources|message.input_image.image_url|computer_call_output.output.image_url|code_interpreter_call.outputs|reasoning.encrypted_content|message.output_text.logprobs))): Specify additional output data to include in the model response. Currently supported values are:
- `web_search_call.action.sources`: Include the sources of the web search tool call.
- `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
- `computer_call_output.output.image_url`: Include image urls from the computer call output.
- `file_search_call.results`: Include the search results of the file search tool call.
- `message.input_image.image_url`: Include image urls from the input message.
- `message.output_text.logprobs`: Include logprobs with assistant messages.
- `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).
- **parallel_tool_calls** (boolean): Whether to allow the model to run tool calls in parallel.

- **store** (boolean): Whether to store the generated model response for later retrieval via
API.

- **instructions** (string): A system (or developer) message inserted into the model's context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

- **stream** (boolean): If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](https://platform.openai.com/docs/api-reference/responses-streaming)
for more information.

- **stream_options** (object): Options for streaming responses. Only set this when you set `stream: true`.

  - **include_obfuscation** (boolean): When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

- **conversation** (string): The unique ID of the conversation.


### Responses

#### 200 - OK

**Response**
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **top_logprobs** (integer): An integer between 0 and 20 specifying the number of most likely tokens to
return at each token position, each with an associated log probability.

- **temperature** (number) (required): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.
 (example: 1)
- **top_p** (number) (required): An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.
 (example: 1)
- **user** (string): This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and  to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).
 (example: "user-1234")
- **safety_identifier** (string): A stable identifier used to help detect users of your application that may be violating OpenAI's usage policies.
The IDs should be a string that uniquely identifies each user. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).
 (example: "safety-identifier-1234")
- **prompt_cache_key** (string): Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).
 (example: "prompt-cache-key-1234")
- **service_tier** (string (auto|default|flex|scale|priority)): Specifies the processing type used for serving the request.
  - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
  - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
  - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
  - When not set, the default behavior is 'auto'.

  When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
 ("auto"|"default"|"flex"|"scale"|"priority")
- **previous_response_id** (string): The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

- **model** (string) (required)
- **reasoning** (object): **gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

  - **effort** (string (minimal|low|medium|high)): Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `minimal`, `low`, `medium`, and `high`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
 ("minimal"|"low"|"medium"|"high")
  - **summary** (string (auto|concise|detailed)): A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is only supported for `computer-use-preview` models.
 ("auto"|"concise"|"detailed")
  - **generate_summary** (string (auto|concise|detailed)): **Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.
 ("auto"|"concise"|"detailed")
- **background** (boolean): Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

- **max_output_tokens** (integer): An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

- **max_tool_calls** (integer): The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

- **text** (object): Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:
- [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

  - **format** (object): Default response format. Used to generate text responses.

    - **type** (string (text)) (required): The type of response format being defined. Always `text`. ("text")
  - **verbosity** (string (low|medium|high)): Constrains the verbosity of the model's response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.
 ("low"|"medium"|"high")
- **tools** (array (object)) (required): An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

We support the following categories of tools:
- **Built-in tools**: Tools that are provided by OpenAI that extend the
  model's capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
- **MCP Tools**: Integrations with third-party systems via custom MCP servers
  or predefined connectors such as Google Drive and SharePoint. Learn more about
  [MCP Tools](https://platform.openai.com/docs/guides/tools-connectors-mcp).
- **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code with strongly typed arguments
  and outputs. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling). You can also use
  custom tools to call your own code.

  Array items:
    - **type** (string (function)) (required): The type of the function tool. Always `function`. ("function")
    - **name** (string) (required): The name of the function to call.
    - **description** (string): A description of the function. Used by the model to determine whether or not to call the function.
    - **parameters** (object) (required): A JSON schema object describing the parameters of the function.
    - **strict** (boolean) (required): Whether to enforce strict parameter validation. Default `true`.
- **tool_choice** (string (none|auto|required)) (required): Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.
 ("none"|"auto"|"required")
- **prompt** (object): Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

  - **id** (string) (required): The unique identifier of the prompt template to use.
  - **version** (string): Optional version of the prompt template.
  - **variables** (object): Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

- **truncation** (string (auto|disabled)): The truncation strategy to use for the model response.
- `auto`: If the input to this Response exceeds
  the model's context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
- `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.
 ("auto"|"disabled")
- **id** (string) (required): Unique identifier for this Response.

- **object** (string (response)) (required): The object type of this resource - always set to `response`.
 ("response")
- **status** (string (completed|failed|in_progress|cancelled|queued|incomplete)): The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.
 ("completed"|"failed"|"in_progress"|"cancelled"|"queued"|"incomplete")
- **created_at** (number) (required): Unix timestamp (in seconds) of when this Response was created.

- **error** (object) (required): An error object returned when the model fails to generate a Response.

  - **code** (string (server_error|rate_limit_exceeded|invalid_prompt|vector_store_timeout|invalid_image|invalid_image_format|invalid_base64_image|invalid_image_url|image_too_large|image_too_small|image_parse_error|image_content_policy_violation|invalid_image_mode|image_file_too_large|unsupported_image_media_type|empty_image_file|failed_to_download_image|image_file_not_found)) (required): The error code for the response.
 ("server_error"|"rate_limit_exceeded"|"invalid_prompt"|"vector_store_timeout"|"invalid_image"|"invalid_image_format"|"invalid_base64_image"|"invalid_image_url"|"image_too_large"|"image_too_small"|"image_parse_error"|"image_content_policy_violation"|"invalid_image_mode"|"image_file_too_large"|"unsupported_image_media_type"|"empty_image_file"|"failed_to_download_image"|"image_file_not_found")
  - **message** (string) (required): A human-readable description of the error.

- **incomplete_details** (object) (required): Details about why the response is incomplete.

  - **reason** (string (max_output_tokens|content_filter)): The reason why the response is incomplete. ("max_output_tokens"|"content_filter")
- **output** (array (object)) (required): An array of content items generated by the model.

- The length and order of items in the `output` array is dependent
  on the model's response.
- Rather than accessing the first item in the `output` array and
  assuming it's an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

  Array items:
    - **id** (string) (required): The unique ID of the output message.

    - **type** (string (message)) (required): The type of the output message. Always `message`.
 ("message")
    - **role** (string (assistant)) (required): The role of the output message. Always `assistant`.
 ("assistant")
    - **content** (array (object)) (required): The content of the output message.

      Array items:
        - **type** (string (output_text)) (required): The type of the output text. Always `output_text`. ("output_text")
        - **text** (string) (required): The text output from the model.
        - **annotations** (array (object)) (required): The annotations of the text output.
          Array items:
            - **type** (string (file_citation)) (required): The type of the file citation. Always `file_citation`. ("file_citation")
            - **file_id** (string) (required): The ID of the file.
            - **index** (integer) (required): The index of the file in the list of files.
            - **filename** (string) (required): The filename of the file cited.
        - **logprobs** (array (object))
          Array items:
            - **token** (string) (required)
            - **logprob** (number) (required)
            - **bytes** (array (integer)) (required)
            - **top_logprobs** (array (object)) (required)
              Array items:
                - **token** (string) (required)
                - **logprob** (number) (required)
                - **bytes** (array (integer)) (required)
    - **status** (string (in_progress|completed|incomplete)) (required): The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.
 ("in_progress"|"completed"|"incomplete")
- **instructions** (string) (required): A text input to the model, equivalent to a text input with the
`developer` role.

- **output_text** (string): SDK-only convenience property that contains the aggregated text output
from all `output_text` items in the `output` array, if any are present.
Supported in the Python and JavaScript SDKs.

- **usage** (object): Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

  - **input_tokens** (integer) (required): The number of input tokens.
  - **input_tokens_details** (object) (required): A detailed breakdown of the input tokens.
    - **cached_tokens** (integer) (required): The number of tokens that were retrieved from the cache. 
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

  - **output_tokens** (integer) (required): The number of output tokens.
  - **output_tokens_details** (object) (required): A detailed breakdown of the output tokens.
    - **reasoning_tokens** (integer) (required): The number of reasoning tokens.
  - **total_tokens** (integer) (required): The total number of tokens used.
- **parallel_tool_calls** (boolean) (required): Whether to allow the model to run tool calls in parallel.

- **conversation** (object): The conversation that this response belongs to. Input items and output items from this response are automatically added to this conversation.
  - **id** (string) (required): The unique ID of the conversation.

**ResponseStreamEvent**
- **type** (string (response.audio.delta)) (required): The type of the event. Always `response.audio.delta`.
 ("response.audio.delta")
- **sequence_number** (integer) (required): A sequence number for this chunk of the stream response.

- **delta** (string) (required): A chunk of Base64 encoded response audio bytes.


### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/responses" \
  -H "Content-Type: application/json" \
  -d '{
  "metadata": "value",
  "top_logprobs": "0",
  "temperature": 1,
  "top_p": 1,
  "user": "user-1234",
  "safety_identifier": "safety-identifier-1234",
  "prompt_cache_key": "prompt-cache-key-1234",
  "service_tier": "auto",
  "previous_response_id": "string",
  "model": "string",
  "reasoning": {
    "effort": "medium",
    "summary": "auto",
    "generate_summary": "auto"
  },
  "background": "false",
  "max_output_tokens": "0",
  "max_tool_calls": "0",
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "medium"
  },
  "tools": [
    {
      "type": "function",
      "name": "string",
      "description": "string",
      "parameters": "value",
      "strict": "true"
    }
  ],
  "tool_choice": "none",
  "prompt": {
    "id": "string",
    "version": "string",
    "variables": "value"
  },
  "truncation": "disabled",
  "input": "string",
  "include": [
    "file_search_call.results"
  ],
  "parallel_tool_calls": "true",
  "store": "true",
  "instructions": "string",
  "stream": "false",
  "stream_options": {
    "include_obfuscation": "true"
  },
  "conversation": "string"
}'
```

```

--------------------------------

### GET /organization/projects/{project_id}/certificates

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List certificates for this project.

```markdown
### Parameters

- **project_id** (string, path, required): The ID of the project.
- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.


### Responses

#### 200 - Certificates listed successfully.

**ListCertificatesResponse**
- **data** (array (object)) (required)
  Array items:
    - **object** (string (certificate|organization.certificate|organization.project.certificate)) (required): The object type.

- If creating, updating, or getting a specific certificate, the object type is `certificate`.
- If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
- If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.
 ("certificate"|"organization.certificate"|"organization.project.certificate")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **name** (string) (required): The name of the certificate.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) of when the certificate was uploaded.
    - **certificate_details** (object) (required)
      - **valid_at** (integer): The Unix timestamp (in seconds) of when the certificate becomes valid.
      - **expires_at** (integer): The Unix timestamp (in seconds) of when the certificate expires.
      - **content** (string): The content of the certificate in PEM format.
    - **active** (boolean): Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.
- **first_id** (string) (example: "cert_abc")
- **last_id** (string) (example: "cert_abc")
- **has_more** (boolean) (required)
- **object** (string (list)) (required) ("list")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/projects/{project_id}/certificates?limit=20&after=string&order=desc"
```

```

--------------------------------

### POST /videos

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create a video

```markdown
### Request Body

**Content-Type:** multipart/form-data

- **model** (string (sora-2|sora-2-pro)) ("sora-2"|"sora-2-pro")
- **prompt** (string) (required): Text prompt that describes the video to generate.
- **input_reference** (string (binary)): Optional image reference that guides generation.
- **seconds** (string (4|8|12)) ("4"|"8"|"12")
- **size** (string (720x1280|1280x720|1024x1792|1792x1024)) ("720x1280"|"1280x720"|"1024x1792"|"1792x1024")

**Content-Type:** application/json

- **model** (string (sora-2|sora-2-pro)) ("sora-2"|"sora-2-pro")
- **prompt** (string) (required): Text prompt that describes the video to generate.
- **input_reference** (string (binary)): Optional image reference that guides generation.
- **seconds** (string (4|8|12)) ("4"|"8"|"12")
- **size** (string (720x1280|1280x720|1024x1792|1792x1024)) ("720x1280"|"1280x720"|"1024x1792"|"1792x1024")

### Responses

#### 200 - Success

**VideoResource**
- **id** (string) (required): Unique identifier for the video job.
- **object** (string (video)) (required): The object type, which is always `video`. ("video")
- **model** (string (sora-2|sora-2-pro)) (required) ("sora-2"|"sora-2-pro")
- **status** (string (queued|in_progress|completed|failed)) (required) ("queued"|"in_progress"|"completed"|"failed")
- **progress** (integer) (required): Approximate completion percentage for the generation task.
- **created_at** (integer) (required): Unix timestamp (seconds) for when the job was created.
- **completed_at** (integer) (required): Unix timestamp (seconds) for when the job completed, if finished.
- **expires_at** (integer) (required): Unix timestamp (seconds) for when the downloadable assets expire, if set.
- **size** (string (720x1280|1280x720|1024x1792|1792x1024)) (required) ("720x1280"|"1280x720"|"1024x1792"|"1792x1024")
- **seconds** (string (4|8|12)) (required) ("4"|"8"|"12")
- **remixed_from_video_id** (string) (required): Identifier of the source video if this video is a remix.
- **error** (object) (required)
  - **code** (string) (required)
  - **message** (string) (required)

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/videos" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "sora-2",
  "prompt": "string",
  "input_reference": "string",
  "seconds": "4",
  "size": "720x1280"
}'
```

```

--------------------------------

### GET /fine_tuning/jobs

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List your organization's fine-tuning jobs


```markdown
### Parameters

- **after** (string, query, optional): Identifier for the last job from the previous pagination request.
- **limit** (integer, query, optional): Number of fine-tuning jobs to retrieve.
- **metadata** (object, query, optional): Optional metadata filter. To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to indicate no metadata.


### Responses

#### 200 - OK

**ListPaginatedFineTuningJobsResponse**
- **data** (array (object)) (required)
  Array items:
    - **id** (string) (required): The object identifier, which can be referenced in the API endpoints.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the fine-tuning job was created.
    - **error** (object) (required): For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.
      - **code** (string) (required): A machine-readable error code.
      - **message** (string) (required): A human-readable error message.
      - **param** (string) (required): The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.
    - **fine_tuned_model** (string) (required): The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.
    - **finished_at** (integer) (required): The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.
    - **hyperparameters** (object) (required): The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.
      - **batch_size** (string (auto)) ("auto")
      - **learning_rate_multiplier** (string (auto)) ("auto")
      - **n_epochs** (string (auto)) ("auto")
    - **model** (string) (required): The base model that is being fine-tuned.
    - **object** (string (fine_tuning.job)) (required): The object type, which is always "fine_tuning.job". ("fine_tuning.job")
    - **organization_id** (string) (required): The organization that owns the fine-tuning job.
    - **result_files** (array (string)) (required): The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).
    - **status** (string (validating_files|queued|running|succeeded|failed|cancelled)) (required): The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`. ("validating_files"|"queued"|"running"|"succeeded"|"failed"|"cancelled")
    - **trained_tokens** (integer) (required): The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.
    - **training_file** (string) (required): The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).
    - **validation_file** (string) (required): The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).
    - **integrations** (array (object)): A list of integrations to enable for this fine-tuning job.
      Array items:
        - **type** (string (wandb)) (required): The type of the integration being enabled for the fine-tuning job ("wandb")
        - **wandb** (object) (required): The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

          - **project** (string) (required): The name of the project that the new run will be created under.
 (example: "my-wandb-project")
          - **name** (string): A display name to set for the run. If not set, we will use the Job ID as the name.

          - **entity** (string): The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

          - **tags** (array (string)): A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

    - **seed** (integer) (required): The seed used for the fine-tuning job.
    - **estimated_finish** (integer): The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.
    - **method** (object): The method used for fine-tuning.
      - **type** (string (supervised|dpo|reinforcement)) (required): The type of method. Is either `supervised`, `dpo`, or `reinforcement`. ("supervised"|"dpo"|"reinforcement")
      - **supervised** (object): Configuration for the supervised fine-tuning method.
        - **hyperparameters** (object): The hyperparameters used for the fine-tuning job.
          - **batch_size** (string (auto)) ("auto")
          - **learning_rate_multiplier** (string (auto)) ("auto")
          - **n_epochs** (string (auto)) ("auto")
      - **dpo** (object): Configuration for the DPO fine-tuning method.
        - **hyperparameters** (object): The hyperparameters used for the DPO fine-tuning job.
          - **beta** (string (auto)) ("auto")
          - **batch_size** (string (auto)) ("auto")
          - **learning_rate_multiplier** (string (auto)) ("auto")
          - **n_epochs** (string (auto)) ("auto")
      - **reinforcement** (object): Configuration for the reinforcement fine-tuning method.
        - **grader** (object) (required): A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - **type** (string (string_check)) (required): The object type, which is always `string_check`. ("string_check")
          - **name** (string) (required): The name of the grader.
          - **input** (string) (required): The input text. This may include template strings.
          - **reference** (string) (required): The reference text. This may include template strings.
          - **operation** (string (eq|ne|like|ilike)) (required): The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`. ("eq"|"ne"|"like"|"ilike")
        - **hyperparameters** (object): The hyperparameters used for the reinforcement fine-tuning job.
          - **batch_size** (string (auto)) ("auto")
          - **learning_rate_multiplier** (string (auto)) ("auto")
          - **n_epochs** (string (auto)) ("auto")
          - **reasoning_effort** (string (default|low|medium|high)): Level of reasoning effort.
 ("default"|"low"|"medium"|"high")
          - **compute_multiplier** (string (auto)) ("auto")
          - **eval_interval** (string (auto)) ("auto")
          - **eval_samples** (string (auto)) ("auto")
    - **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **has_more** (boolean) (required)
- **object** (string (list)) (required) ("list")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/fine_tuning/jobs?after=string&limit=20&metadata=value"
```

```

--------------------------------

### GET /organization/projects/{project_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a project.

```markdown
### Parameters

- **project_id** (string, path, required): The ID of the project.

### Responses

#### 200 - Project retrieved successfully.

**Project**
- **id** (string) (required): The identifier, which can be referenced in API endpoints
- **object** (string (organization.project)) (required): The object type, which is always `organization.project` ("organization.project")
- **name** (string) (required): The name of the project. This appears in reporting.
- **created_at** (integer) (required): The Unix timestamp (in seconds) of when the project was created.
- **archived_at** (integer): The Unix timestamp (in seconds) of when the project was archived or `null`.
- **status** (string (active|archived)) (required): `active` or `archived` ("active"|"archived")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/projects/{project_id}"
```

```

--------------------------------

### GET /evals/{eval_id}/runs

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get a list of runs for an evaluation.


```markdown
### Parameters

- **eval_id** (string, path, required): The ID of the evaluation to retrieve runs for.
- **after** (string, query, optional): Identifier for the last run from the previous pagination request.
- **limit** (integer, query, optional): Number of runs to retrieve.
- **order** (string (asc|desc), query, optional): Sort order for runs by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
- **status** (string (queued|in_progress|completed|canceled|failed), query, optional): Filter runs by status. One of `queued` | `in_progress` | `failed` | `completed` | `canceled`.

### Responses

#### 200 - A list of runs for the evaluation

**EvalRunList**
- **object** (string (list)) (required): The type of this object. It is always set to "list".
 ("list")
- **data** (array (object)) (required): An array of eval run objects.

  Array items:
    - **object** (string (eval.run)) (required): The type of the object. Always "eval.run". ("eval.run")
    - **id** (string) (required): Unique identifier for the evaluation run.
    - **eval_id** (string) (required): The identifier of the associated evaluation.
    - **status** (string) (required): The status of the evaluation run.
    - **model** (string) (required): The model that is evaluated, if applicable.
    - **name** (string) (required): The name of the evaluation run.
    - **created_at** (integer) (required): Unix timestamp (in seconds) when the evaluation run was created.
    - **report_url** (string) (required): The URL to the rendered evaluation run report on the UI dashboard.
    - **result_counts** (object) (required): Counters summarizing the outcomes of the evaluation run.
      - **total** (integer) (required): Total number of executed output items.
      - **errored** (integer) (required): Number of output items that resulted in an error.
      - **failed** (integer) (required): Number of output items that failed to pass the evaluation.
      - **passed** (integer) (required): Number of output items that passed the evaluation.
    - **per_model_usage** (array (object)) (required): Usage statistics for each model during the evaluation run.
      Array items:
        - **model_name** (string) (required): The name of the model.
        - **invocation_count** (integer) (required): The number of invocations.
        - **prompt_tokens** (integer) (required): The number of prompt tokens used.
        - **completion_tokens** (integer) (required): The number of completion tokens generated.
        - **total_tokens** (integer) (required): The total number of tokens used.
        - **cached_tokens** (integer) (required): The number of tokens retrieved from cache.
    - **per_testing_criteria_results** (array (object)) (required): Results per testing criteria applied during the evaluation run.
      Array items:
        - **testing_criteria** (string) (required): A description of the testing criteria.
        - **passed** (integer) (required): Number of tests passed for this criteria.
        - **failed** (integer) (required): Number of tests failed for this criteria.
    - **data_source** (object) (required): A JsonlRunDataSource object with that specifies a JSONL file that matches the eval 

      - **type** (string (jsonl)) (required): The type of data source. Always `jsonl`. ("jsonl")
      - **source** (object) (required)
        - **type** (string (file_content)) (required): The type of jsonl source. Always `file_content`. ("file_content")
        - **content** (array (object)) (required): The content of the jsonl file.
          Array items:
            - **item** (object) (required)
            - **sample** (object)
    - **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

    - **error** (object) (required): An object representing an error response from the Eval API.

      - **code** (string) (required): The error code.
      - **message** (string) (required): The error message.
- **first_id** (string) (required): The identifier of the first eval run in the data array.
- **last_id** (string) (required): The identifier of the last eval run in the data array.
- **has_more** (boolean) (required): Indicates whether there are more evals available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/evals/{eval_id}/runs?after=string&limit=20&order=asc&status=queued"
```

```

--------------------------------

### GET /organization/usage/code_interpreter_sessions

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get code interpreter sessions usage details for the organization.

```markdown
### Parameters

- **start_time** (integer, query, required): Start time (Unix seconds) of the query time range, inclusive.
- **end_time** (integer, query, optional): End time (Unix seconds) of the query time range, exclusive.
- **bucket_width** (string (1m|1h|1d), query, optional): Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.
- **project_ids** (array (string), query, optional): Return only usage for these projects.
- **group_by** (array (string (project_id)), query, optional): Group the usage data by the specified fields. Support fields include `project_id`.
- **limit** (integer, query, optional): Specifies the number of buckets to return.
- `bucket_width=1d`: default: 7, max: 31
- `bucket_width=1h`: default: 24, max: 168
- `bucket_width=1m`: default: 60, max: 1440

- **page** (string, query, optional): A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

### Responses

#### 200 - Usage data retrieved successfully.

**UsageResponse**
- **object** (string (page)) (required) ("page")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (bucket)) (required) ("bucket")
    - **start_time** (integer) (required)
    - **end_time** (integer) (required)
    - **result** (array (object)) (required)
      Array items:
        - **object** (string (organization.usage.completions.result)) (required) ("organization.usage.completions.result")
        - **input_tokens** (integer) (required): The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_cached_tokens** (integer): The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.
        - **output_tokens** (integer) (required): The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.
        - **input_audio_tokens** (integer): The aggregated number of audio input tokens used, including cached tokens.
        - **output_audio_tokens** (integer): The aggregated number of audio output tokens used.
        - **num_model_requests** (integer) (required): The count of requests made to the model.
        - **project_id** (string): When `group_by=project_id`, this field provides the project ID of the grouped usage result.
        - **user_id** (string): When `group_by=user_id`, this field provides the user ID of the grouped usage result.
        - **api_key_id** (string): When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.
        - **model** (string): When `group_by=model`, this field provides the model name of the grouped usage result.
        - **batch** (boolean): When `group_by=batch`, this field tells whether the grouped usage result is batch or not.
        - **service_tier** (string): When `group_by=service_tier`, this field provides the service tier of the grouped usage result.
- **has_more** (boolean) (required)
- **next_page** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/usage/code_interpreter_sessions?start_time=0&end_time=0&bucket_width=1d&project_ids=item1,item2&group_by=item1,item2&limit=0&page=string"
```

```

--------------------------------

### POST /vector_stores

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create a vector store.

```markdown
### Request Body

**Content-Type:** application/json

- **file_ids** (array (string)): A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.
- **name** (string): The name of the vector store.
- **description** (string): A description for the vector store. Can be used to describe the vector store's purpose.
- **expires_after** (object): The expiration policy for a vector store.
  - **anchor** (string (last_active_at)) (required): Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`. ("last_active_at")
  - **days** (integer) (required): The number of days after the anchor time that the vector store will expire.
- **chunking_strategy** (object): The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.
  - **type** (string (auto)) (required): Always `auto`. ("auto")
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Responses

#### 200 - OK

**VectorStoreObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (vector_store)) (required): The object type, which is always `vector_store`. ("vector_store")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store was created.
- **name** (string) (required): The name of the vector store.
- **usage_bytes** (integer) (required): The total number of bytes used by the files in the vector store.
- **file_counts** (object) (required)
  - **in_progress** (integer) (required): The number of files that are currently being processed.
  - **completed** (integer) (required): The number of files that have been successfully processed.
  - **failed** (integer) (required): The number of files that have failed to process.
  - **cancelled** (integer) (required): The number of files that were cancelled.
  - **total** (integer) (required): The total number of files.
- **status** (string (expired|in_progress|completed)) (required): The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use. ("expired"|"in_progress"|"completed")
- **expires_after** (object): The expiration policy for a vector store.
  - **anchor** (string (last_active_at)) (required): Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`. ("last_active_at")
  - **days** (integer) (required): The number of days after the anchor time that the vector store will expire.
- **expires_at** (integer): The Unix timestamp (in seconds) for when the vector store will expire.
- **last_active_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store was last active.
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/vector_stores" \
  -H "Content-Type: application/json" \
  -d '{
  "file_ids": [
    "string"
  ],
  "name": "string",
  "description": "string",
  "expires_after": {
    "anchor": "last_active_at",
    "days": "0"
  },
  "chunking_strategy": {
    "type": "auto"
  },
  "metadata": "value"
}'
```

```

--------------------------------

### GET /models/{model}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

```markdown
### Parameters

- **model** (string, path, required): The ID of the model to use for this request (example: "gpt-4o-mini")

### Responses

#### 200 - OK

**Model**

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/models/{model}"
```

```

--------------------------------

### GET /fine_tuning/jobs/{fine_tuning_job_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get info about a fine-tuning job.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)


```markdown
### Parameters

- **fine_tuning_job_id** (string, path, required): The ID of the fine-tuning job.
 (example: "ft-AF1WoRqd3aJAHsqc9NY7iL8F")

### Responses

#### 200 - OK

**FineTuningJob**
- **id** (string) (required): The object identifier, which can be referenced in the API endpoints.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the fine-tuning job was created.
- **error** (object) (required): For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.
  - **code** (string) (required): A machine-readable error code.
  - **message** (string) (required): A human-readable error message.
  - **param** (string) (required): The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.
- **fine_tuned_model** (string) (required): The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.
- **finished_at** (integer) (required): The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.
- **hyperparameters** (object) (required): The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.
  - **batch_size** (string (auto)) ("auto")
  - **learning_rate_multiplier** (string (auto)) ("auto")
  - **n_epochs** (string (auto)) ("auto")
- **model** (string) (required): The base model that is being fine-tuned.
- **object** (string (fine_tuning.job)) (required): The object type, which is always "fine_tuning.job". ("fine_tuning.job")
- **organization_id** (string) (required): The organization that owns the fine-tuning job.
- **result_files** (array (string)) (required): The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).
- **status** (string (validating_files|queued|running|succeeded|failed|cancelled)) (required): The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`. ("validating_files"|"queued"|"running"|"succeeded"|"failed"|"cancelled")
- **trained_tokens** (integer) (required): The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.
- **training_file** (string) (required): The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).
- **validation_file** (string) (required): The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).
- **integrations** (array (object)): A list of integrations to enable for this fine-tuning job.
  Array items:
    - **type** (string (wandb)) (required): The type of the integration being enabled for the fine-tuning job ("wandb")
    - **wandb** (object) (required): The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

      - **project** (string) (required): The name of the project that the new run will be created under.
 (example: "my-wandb-project")
      - **name** (string): A display name to set for the run. If not set, we will use the Job ID as the name.

      - **entity** (string): The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - **tags** (array (string)): A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

- **seed** (integer) (required): The seed used for the fine-tuning job.
- **estimated_finish** (integer): The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.
- **method** (object): The method used for fine-tuning.
  - **type** (string (supervised|dpo|reinforcement)) (required): The type of method. Is either `supervised`, `dpo`, or `reinforcement`. ("supervised"|"dpo"|"reinforcement")
  - **supervised** (object): Configuration for the supervised fine-tuning method.
    - **hyperparameters** (object): The hyperparameters used for the fine-tuning job.
      - **batch_size** (string (auto)) ("auto")
      - **learning_rate_multiplier** (string (auto)) ("auto")
      - **n_epochs** (string (auto)) ("auto")
  - **dpo** (object): Configuration for the DPO fine-tuning method.
    - **hyperparameters** (object): The hyperparameters used for the DPO fine-tuning job.
      - **beta** (string (auto)) ("auto")
      - **batch_size** (string (auto)) ("auto")
      - **learning_rate_multiplier** (string (auto)) ("auto")
      - **n_epochs** (string (auto)) ("auto")
  - **reinforcement** (object): Configuration for the reinforcement fine-tuning method.
    - **grader** (object) (required): A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - **type** (string (string_check)) (required): The object type, which is always `string_check`. ("string_check")
      - **name** (string) (required): The name of the grader.
      - **input** (string) (required): The input text. This may include template strings.
      - **reference** (string) (required): The reference text. This may include template strings.
      - **operation** (string (eq|ne|like|ilike)) (required): The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`. ("eq"|"ne"|"like"|"ilike")
    - **hyperparameters** (object): The hyperparameters used for the reinforcement fine-tuning job.
      - **batch_size** (string (auto)) ("auto")
      - **learning_rate_multiplier** (string (auto)) ("auto")
      - **n_epochs** (string (auto)) ("auto")
      - **reasoning_effort** (string (default|low|medium|high)): Level of reasoning effort.
 ("default"|"low"|"medium"|"high")
      - **compute_multiplier** (string (auto)) ("auto")
      - **eval_interval** (string (auto)) ("auto")
      - **eval_samples** (string (auto)) ("auto")
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}"
```

```

--------------------------------

### POST /completions

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Creates a completion for the provided prompt and parameters.

```markdown
### Request Body

**Content-Type:** application/json

- **model** (string) (required)
- **prompt** (string) (required) (example: "This is a test.")
- **best_of** (integer): Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.

When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return – `best_of` must be greater than `n`.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

- **echo** (boolean): Echo back the prompt in addition to the completion

- **frequency_penalty** (number): Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

[See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation)

- **logit_bias** (object): Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated.

- **logprobs** (integer): Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.

The maximum value for `logprobs` is 5.

- **max_tokens** (integer): The maximum number of [tokens](/tokenizer) that can be generated in the completion.

The token count of your prompt plus `max_tokens` cannot exceed the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.
 (example: 16)
- **n** (integer): How many completions to generate for each prompt.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.
 (example: 1)
- **presence_penalty** (number): Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

[See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation)

- **seed** (integer (int64)): If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.

Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

- **stop** (string) (example: "\n")
- **stream** (boolean): Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

- **stream_options** (object): Options for streaming response. Only set this when you set `stream: true`.

  - **include_usage** (boolean): If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

  - **include_obfuscation** (boolean): When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

- **suffix** (string): The suffix that comes after a completion of inserted text.

This parameter is only supported for `gpt-3.5-turbo-instruct`.
 (example: "test.")
- **temperature** (number): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

We generally recommend altering this or `top_p` but not both.
 (example: 1)
- **top_p** (number): An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or `temperature` but not both.
 (example: 1)
- **user** (string): A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).
 (example: "user-1234")

### Responses

#### 200 - OK

**CreateCompletionResponse**
- **id** (string) (required): A unique identifier for the completion.
- **choices** (array (object)) (required): The list of completion choices the model generated for the input prompt.
  Array items:
    - **finish_reason** (string (stop|length|content_filter)) (required): The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
or `content_filter` if content was omitted due to a flag from our content filters.
 ("stop"|"length"|"content_filter")
    - **index** (integer) (required)
    - **logprobs** (object) (required)
      - **text_offset** (array (integer))
      - **token_logprobs** (array (number))
      - **tokens** (array (string))
      - **top_logprobs** (array (object))
    - **text** (string) (required)
- **created** (integer) (required): The Unix timestamp (in seconds) of when the completion was created.
- **model** (string) (required): The model used for completion.
- **system_fingerprint** (string): This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

- **object** (string (text_completion)) (required): The object type, which is always "text_completion" ("text_completion")
- **usage** (object): Usage statistics for the completion request.
  - **completion_tokens** (integer) (required): Number of tokens in the generated completion.
  - **prompt_tokens** (integer) (required): Number of tokens in the prompt.
  - **total_tokens** (integer) (required): Total number of tokens used in the request (prompt + completion).
  - **completion_tokens_details** (object): Breakdown of tokens used in a completion.
    - **accepted_prediction_tokens** (integer): When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

    - **audio_tokens** (integer): Audio input tokens generated by the model.
    - **reasoning_tokens** (integer): Tokens generated by the model for reasoning.
    - **rejected_prediction_tokens** (integer): When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

  - **prompt_tokens_details** (object): Breakdown of tokens used in the prompt.
    - **audio_tokens** (integer): Audio input tokens present in the prompt.
    - **cached_tokens** (integer): Cached tokens present in the prompt.

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/completions" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "string",
  "prompt": "This is a test.",
  "best_of": "1",
  "echo": "false",
  "frequency_penalty": "0",
  "logit_bias": "null",
  "logprobs": "null",
  "max_tokens": 16,
  "n": 1,
  "presence_penalty": "0",
  "seed": "0",
  "stop": "\n",
  "stream": "false",
  "stream_options": {
    "include_usage": "true",
    "include_obfuscation": "true"
  },
  "suffix": "test.",
  "temperature": 1,
  "top_p": 1,
  "user": "user-1234"
}'
```

```

--------------------------------

### GET /evals/{eval_id}/runs/{run_id}/output_items

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get a list of output items for an evaluation run.


```markdown
### Parameters

- **eval_id** (string, path, required): The ID of the evaluation to retrieve runs for.
- **run_id** (string, path, required): The ID of the run to retrieve output items for.
- **after** (string, query, optional): Identifier for the last output item from the previous pagination request.
- **limit** (integer, query, optional): Number of output items to retrieve.
- **status** (string (fail|pass), query, optional): Filter output items by status. Use `failed` to filter by failed output
items or `pass` to filter by passed output items.

- **order** (string (asc|desc), query, optional): Sort order for output items by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

### Responses

#### 200 - A list of output items for the evaluation run

**EvalRunOutputItemList**
- **object** (string (list)) (required): The type of this object. It is always set to "list".
 ("list")
- **data** (array (object)) (required): An array of eval run output item objects.

  Array items:
    - **object** (string (eval.run.output_item)) (required): The type of the object. Always "eval.run.output_item". ("eval.run.output_item")
    - **id** (string) (required): Unique identifier for the evaluation run output item.
    - **run_id** (string) (required): The identifier of the evaluation run associated with this output item.
    - **eval_id** (string) (required): The identifier of the evaluation group.
    - **created_at** (integer) (required): Unix timestamp (in seconds) when the evaluation run was created.
    - **status** (string) (required): The status of the evaluation run.
    - **datasource_item_id** (integer) (required): The identifier for the data source item.
    - **datasource_item** (object) (required): Details of the input data source item.
    - **results** (array (object)) (required): A list of grader results for this output item.
      Array items:
        - **name** (string) (required): The name of the grader.
        - **type** (string): The grader type (for example, "string-check-grader").
        - **score** (number) (required): The numeric score produced by the grader.
        - **passed** (boolean) (required): Whether the grader considered the output a pass.
        - **sample** (object)
    - **sample** (object) (required): A sample containing the input and output of the evaluation run.
      - **input** (array (object)) (required): An array of input messages.
        Array items:
          - **role** (string) (required): The role of the message sender (e.g., system, user, developer).
          - **content** (string) (required): The content of the message.
      - **output** (array (object)) (required): An array of output messages.
        Array items:
          - **role** (string): The role of the message (e.g. "system", "assistant", "user").
          - **content** (string): The content of the message.
      - **finish_reason** (string) (required): The reason why the sample generation was finished.
      - **model** (string) (required): The model used for generating the sample.
      - **usage** (object) (required): Token usage details for the sample.
        - **total_tokens** (integer) (required): The total number of tokens used.
        - **completion_tokens** (integer) (required): The number of completion tokens generated.
        - **prompt_tokens** (integer) (required): The number of prompt tokens used.
        - **cached_tokens** (integer) (required): The number of tokens retrieved from cache.
      - **error** (object) (required): An object representing an error response from the Eval API.

        - **code** (string) (required): The error code.
        - **message** (string) (required): The error message.
      - **temperature** (number) (required): The sampling temperature used.
      - **max_completion_tokens** (integer) (required): The maximum number of tokens allowed for completion.
      - **top_p** (number) (required): The top_p value used for sampling.
      - **seed** (integer) (required): The seed used for generating the sample.
- **first_id** (string) (required): The identifier of the first eval run output item in the data array.
- **last_id** (string) (required): The identifier of the last eval run output item in the data array.
- **has_more** (boolean) (required): Indicates whether there are more eval run output items available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/evals/{eval_id}/runs/{run_id}/output_items?after=string&limit=20&status=fail&order=asc"
```

```

--------------------------------

### GET /vector_stores

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of vector stores.

```markdown
### Parameters

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **before** (string, query, optional): A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.


### Responses

#### 200 - OK

**ListVectorStoresResponse**

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/vector_stores?limit=20&order=desc&after=string&before=string"
```

```

--------------------------------

### GET /fine_tuning/jobs/{fine_tuning_job_id}/events

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get status updates for a fine-tuning job.


```markdown
### Parameters

- **fine_tuning_job_id** (string, path, required): The ID of the fine-tuning job to get events for.
 (example: "ft-AF1WoRqd3aJAHsqc9NY7iL8F")
- **after** (string, query, optional): Identifier for the last event from the previous pagination request.
- **limit** (integer, query, optional): Number of events to retrieve.

### Responses

#### 200 - OK

**ListFineTuningJobEventsResponse**
- **data** (array (object)) (required)
  Array items:
    - **object** (string (fine_tuning.job.event)) (required): The object type, which is always "fine_tuning.job.event". ("fine_tuning.job.event")
    - **id** (string) (required): The object identifier.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the fine-tuning job was created.
    - **level** (string (info|warn|error)) (required): The log level of the event. ("info"|"warn"|"error")
    - **message** (string) (required): The message of the event.
    - **type** (string (message|metrics)): The type of event. ("message"|"metrics")
    - **data** (object): The data associated with the event.
- **object** (string (list)) (required) ("list")
- **has_more** (boolean) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/events?after=string&limit=20"
```

```

--------------------------------

### GET /evals/{eval_id}/runs/{run_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get an evaluation run by ID.


```markdown
### Parameters

- **eval_id** (string, path, required): The ID of the evaluation to retrieve runs for.
- **run_id** (string, path, required): The ID of the run to retrieve.

### Responses

#### 200 - The evaluation run

**EvalRun**
- **object** (string (eval.run)) (required): The type of the object. Always "eval.run". ("eval.run")
- **id** (string) (required): Unique identifier for the evaluation run.
- **eval_id** (string) (required): The identifier of the associated evaluation.
- **status** (string) (required): The status of the evaluation run.
- **model** (string) (required): The model that is evaluated, if applicable.
- **name** (string) (required): The name of the evaluation run.
- **created_at** (integer) (required): Unix timestamp (in seconds) when the evaluation run was created.
- **report_url** (string) (required): The URL to the rendered evaluation run report on the UI dashboard.
- **result_counts** (object) (required): Counters summarizing the outcomes of the evaluation run.
  - **total** (integer) (required): Total number of executed output items.
  - **errored** (integer) (required): Number of output items that resulted in an error.
  - **failed** (integer) (required): Number of output items that failed to pass the evaluation.
  - **passed** (integer) (required): Number of output items that passed the evaluation.
- **per_model_usage** (array (object)) (required): Usage statistics for each model during the evaluation run.
  Array items:
    - **model_name** (string) (required): The name of the model.
    - **invocation_count** (integer) (required): The number of invocations.
    - **prompt_tokens** (integer) (required): The number of prompt tokens used.
    - **completion_tokens** (integer) (required): The number of completion tokens generated.
    - **total_tokens** (integer) (required): The total number of tokens used.
    - **cached_tokens** (integer) (required): The number of tokens retrieved from cache.
- **per_testing_criteria_results** (array (object)) (required): Results per testing criteria applied during the evaluation run.
  Array items:
    - **testing_criteria** (string) (required): A description of the testing criteria.
    - **passed** (integer) (required): Number of tests passed for this criteria.
    - **failed** (integer) (required): Number of tests failed for this criteria.
- **data_source** (object) (required): A JsonlRunDataSource object with that specifies a JSONL file that matches the eval 

  - **type** (string (jsonl)) (required): The type of data source. Always `jsonl`. ("jsonl")
  - **source** (object) (required)
    - **type** (string (file_content)) (required): The type of jsonl source. Always `file_content`. ("file_content")
    - **content** (array (object)) (required): The content of the jsonl file.
      Array items:
        - **item** (object) (required)
        - **sample** (object)
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **error** (object) (required): An object representing an error response from the Eval API.

  - **code** (string) (required): The error code.
  - **message** (string) (required): The error message.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/evals/{eval_id}/runs/{run_id}"
```

```

--------------------------------

### Schema: ListFineTuningJobEventsResponse

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Schema definition for ListFineTuningJobEventsResponse

```markdown
## Schema: ListFineTuningJobEventsResponse

Schema definition for ListFineTuningJobEventsResponse

**Type:** object

- **data** (array (object)) (required)
  Array items:
    - **object** (string (fine_tuning.job.event)) (required): The object type, which is always "fine_tuning.job.event". ("fine_tuning.job.event")
    - **id** (string) (required): The object identifier.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the fine-tuning job was created.
    - **level** (string (info|warn|error)) (required): The log level of the event. ("info"|"warn"|"error")
    - **message** (string) (required): The message of the event.
    - **type** (string (message|metrics)): The type of event. ("message"|"metrics")
    - **data** (object): The data associated with the event.
- **object** (string (list)) (required) ("list")
- **has_more** (boolean) (required)

```

--------------------------------

### GET /organization/invites

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of invites in the organization.

```markdown
### Parameters

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.


### Responses

#### 200 - Invites listed successfully.

**InviteListResponse**
- **object** (string (list)) (required): The object type, which is always `list` ("list")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (organization.invite)) (required): The object type, which is always `organization.invite` ("organization.invite")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **email** (string) (required): The email address of the individual to whom the invite was sent
    - **role** (string (owner|reader)) (required): `owner` or `reader` ("owner"|"reader")
    - **status** (string (accepted|expired|pending)) (required): `accepted`,`expired`, or `pending` ("accepted"|"expired"|"pending")
    - **invited_at** (integer) (required): The Unix timestamp (in seconds) of when the invite was sent.
    - **expires_at** (integer) (required): The Unix timestamp (in seconds) of when the invite expires.
    - **accepted_at** (integer): The Unix timestamp (in seconds) of when the invite was accepted.
    - **projects** (array (object)): The projects that were granted membership upon acceptance of the invite.
      Array items:
        - **id** (string): Project's public ID
        - **role** (string (member|owner)): Project membership role ("member"|"owner")
- **first_id** (string): The first `invite_id` in the retrieved `list`
- **last_id** (string): The last `invite_id` in the retrieved `list`
- **has_more** (boolean): The `has_more` property is used for pagination to indicate there are additional results.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/invites?limit=20&after=string"
```

```

--------------------------------

### GET /chat/completions/{completion_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get a stored chat completion. Only Chat Completions that have been created
with the `store` parameter set to `true` will be returned.


```markdown
### Parameters

- **completion_id** (string, path, required): The ID of the chat completion to retrieve.

### Responses

#### 200 - A chat completion

**CreateChatCompletionResponse**
- **id** (string) (required): A unique identifier for the chat completion.
- **choices** (array (object)) (required): A list of chat completion choices. Can be more than one if `n` is greater than 1.
  Array items:
    - **finish_reason** (string (stop|length|tool_calls|content_filter|function_call)) (required): The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
 ("stop"|"length"|"tool_calls"|"content_filter"|"function_call")
    - **index** (integer) (required): The index of the choice in the list of choices.
    - **message** (object) (required): A chat completion message generated by the model.
      - **content** (string) (required): The contents of the message.
      - **refusal** (string) (required): The refusal message generated by the model.
      - **tool_calls** (array (object)): The tool calls generated by the model, such as function calls.
        Array items:
          - **id** (string) (required): The ID of the tool call.
          - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
          - **function** (object) (required): The function that the model called.
            - **name** (string) (required): The name of the function to call.
            - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
      - **annotations** (array (object)): Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

        Array items:
          - **type** (string (url_citation)) (required): The type of the URL citation. Always `url_citation`. ("url_citation")
          - **url_citation** (object) (required): A URL citation when using web search.
            - **end_index** (integer) (required): The index of the last character of the URL citation in the message.
            - **start_index** (integer) (required): The index of the first character of the URL citation in the message.
            - **url** (string) (required): The URL of the web resource.
            - **title** (string) (required): The title of the web resource.
      - **role** (string (assistant)) (required): The role of the author of this message. ("assistant")
      - **function_call** (object): Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.
        - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
        - **name** (string) (required): The name of the function to call.
      - **audio** (object): If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

        - **id** (string) (required): Unique identifier for this audio response.
        - **expires_at** (integer) (required): The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

        - **data** (string) (required): Base64 encoded audio bytes generated by the model, in the format
specified in the request.

        - **transcript** (string) (required): Transcript of the audio generated by the model.
    - **logprobs** (object) (required): Log probability information for the choice.
      - **content** (array (object)) (required): A list of message content tokens with log probability information.
        Array items:
          - **token** (string) (required): The token.
          - **logprob** (number) (required): The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.
          - **bytes** (array (integer)) (required): A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.
          - **top_logprobs** (array (object)) (required): List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.
            Array items:
              - **token** (string) (required): The token.
              - **logprob** (number) (required): The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.
              - **bytes** (array (integer)) (required): A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.
      - **refusal** (array (object)) (required): A list of message refusal tokens with log probability information.
        Array items:
- **created** (integer) (required): The Unix timestamp (in seconds) of when the chat completion was created.
- **model** (string) (required): The model used for the chat completion.
- **service_tier** (string (auto|default|flex|scale|priority)): Specifies the processing type used for serving the request.
  - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
  - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
  - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
  - When not set, the default behavior is 'auto'.

  When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.
 ("auto"|"default"|"flex"|"scale"|"priority")
- **system_fingerprint** (string): This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

- **object** (string (chat.completion)) (required): The object type, which is always `chat.completion`. ("chat.completion")
- **usage** (object): Usage statistics for the completion request.
  - **completion_tokens** (integer) (required): Number of tokens in the generated completion.
  - **prompt_tokens** (integer) (required): Number of tokens in the prompt.
  - **total_tokens** (integer) (required): Total number of tokens used in the request (prompt + completion).
  - **completion_tokens_details** (object): Breakdown of tokens used in a completion.
    - **accepted_prediction_tokens** (integer): When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

    - **audio_tokens** (integer): Audio input tokens generated by the model.
    - **reasoning_tokens** (integer): Tokens generated by the model for reasoning.
    - **rejected_prediction_tokens** (integer): When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

  - **prompt_tokens_details** (object): Breakdown of tokens used in the prompt.
    - **audio_tokens** (integer): Audio input tokens present in the prompt.
    - **cached_tokens** (integer): Cached tokens present in the prompt.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/chat/completions/{completion_id}"
```

```

--------------------------------

### Schema: Realtime call creation request

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Parameters required to initiate a realtime call and receive the SDP answer
needed to complete a WebRTC peer connection. Provide an SDP offer generated
by your client and optionally configure the session that will answer the call.

```markdown
## Schema: Realtime call creation request

Parameters required to initiate a realtime call and receive the SDP answer
needed to complete a WebRTC peer connection. Provide an SDP offer generated
by your client and optionally configure the session that will answer the call.

**Type:** object

- **sdp** (string) (required): WebRTC Session Description Protocol (SDP) offer generated by the caller.
- **session** (object): Realtime session object configuration.
  - **type** (string (realtime)) (required): The type of session to create. Always `realtime` for the Realtime API.
 ("realtime")
  - **output_modalities** (array (string (text|audio))): The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

  - **model** (string)
  - **instructions** (string): The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. "be extremely succinct", "act friendly", "here are examples of good responses") and on audio behavior (e.g. "talk quickly", "inject emotion into your voice", "laugh frequently"). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

  - **audio** (object): Configuration for input and output audio.

    - **input** (object)
      - **format** (object): The PCM audio format. Only a 24kHz sample rate is supported.
        - **type** (string (audio/pcm)): The audio format. Always `audio/pcm`. ("audio/pcm")
        - **rate** (integer): The sample rate of the audio. Always `24000`. ("24000")
      - **transcription** (object)
        - **model** (string (whisper-1|gpt-4o-mini-transcribe|gpt-4o-transcribe|gpt-4o-transcribe-diarize)): The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.
 ("whisper-1"|"gpt-4o-mini-transcribe"|"gpt-4o-transcribe"|"gpt-4o-transcribe-diarize")
        - **language** (string): The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

        - **prompt** (string): An optional text to guide the model's style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example "expect words related to technology".

      - **noise_reduction** (object): Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

        - **type** (string (near_field|far_field)): Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.
 ("near_field"|"far_field")
      - **turn_detection** (object): Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.
        - **type** (string) (required): Type of turn detection, `server_vad` to turn on simple Server VAD.

        - **threshold** (number): Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

        - **prefix_padding_ms** (integer): Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

        - **silence_duration_ms** (integer): Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

        - **create_response** (boolean): Whether or not to automatically generate a response when a VAD stop event occurs.

        - **interrupt_response** (boolean): Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

        - **idle_timeout_ms** (integer): Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response's audio has finished playing,
i.e. it's set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

    - **output** (object)
      - **format** (object): The PCM audio format. Only a 24kHz sample rate is supported.
      - **voice** (string)
      - **speed** (number): The speed of the model's spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it's
also possible to prompt the model to speak faster or slower.

  - **include** (array (string (item.input_audio_transcription.logprobs))): Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

  - **tracing** (string (auto)): Enables tracing and sets default values for tracing configuration options. Always `auto`.
 ("auto")
  - **tools** (array (object)): Tools available to the model.
    Array items:
      - **type** (string (function)): The type of the tool, i.e. `function`. ("function")
      - **name** (string): The name of the function.
      - **description** (string): The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

      - **parameters** (object): Parameters of the function in JSON Schema.
  - **tool_choice** (string (none|auto|required)): Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.
 ("none"|"auto"|"required")
  - **max_output_tokens** (integer)
  - **truncation** (string (auto|disabled)): The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit. ("auto"|"disabled")
  - **prompt** (object): Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

    - **id** (string) (required): The unique identifier of the prompt template to use.
    - **version** (string): Optional version of the prompt template.
    - **variables** (object): Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.


```

--------------------------------

### Schema: RealtimeBetaServerEventConversationItemInputAudioTranscriptionCompleted

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (in `server_vad` mode). Transcription runs
asynchronously with Response creation, so this event may come before or after
the Response events.

Realtime API models accept audio natively, and thus input transcription is a
separate process run on a separate ASR (Automatic Speech Recognition) model.
The transcript may diverge somewhat from the model's interpretation, and
should be treated as a rough guide.


```markdown
## Schema: RealtimeBetaServerEventConversationItemInputAudioTranscriptionCompleted

This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (in `server_vad` mode). Transcription runs
asynchronously with Response creation, so this event may come before or after
the Response events.

Realtime API models accept audio natively, and thus input transcription is a
separate process run on a separate ASR (Automatic Speech Recognition) model.
The transcript may diverge somewhat from the model's interpretation, and
should be treated as a rough guide.


**Type:** object

- **event_id** (string) (required): The unique ID of the server event.
- **type** (string (conversation.item.input_audio_transcription.completed)) (required): The event type, must be
`conversation.item.input_audio_transcription.completed`.
 ("conversation.item.input_audio_transcription.completed")
- **item_id** (string) (required): The ID of the user message item containing the audio.
- **content_index** (integer) (required): The index of the content part containing the audio.
- **transcript** (string) (required): The transcribed text.
- **logprobs** (array (object)): The log probabilities of the transcription.
  Array items:
    - **token** (string) (required): The token that was used to generate the log probability.

    - **logprob** (number) (required): The log probability of the token.

    - **bytes** (array (integer)) (required): The bytes that were used to generate the log probability.

- **usage** (object) (required): Usage statistics for models billed by token usage.
  - **type** (string (tokens)) (required): The type of the usage object. Always `tokens` for this variant. ("tokens")
  - **input_tokens** (integer) (required): Number of input tokens billed for this request.
  - **input_token_details** (object): Details about the input tokens billed for this request.
    - **text_tokens** (integer): Number of text tokens billed for this request.
    - **audio_tokens** (integer): Number of audio tokens billed for this request.
  - **output_tokens** (integer) (required): Number of output tokens generated.
  - **total_tokens** (integer) (required): Total number of tokens used (input + output).

```

--------------------------------

### Schema: Realtime system message item

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation's behavior, use instructions, but for smaller updates (e.g. "the user is now asking about a different topic"), use system messages.

```markdown
## Schema: Realtime system message item

A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation's behavior, use instructions, but for smaller updates (e.g. "the user is now asking about a different topic"), use system messages.

**Type:** object

- **id** (string): The unique ID of the item. This may be provided by the client or generated by the server.
- **object** (string (realtime.item)): Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item. ("realtime.item")
- **type** (string (message)) (required): The type of the item. Always `message`. ("message")
- **status** (string (completed|incomplete|in_progress)): The status of the item. Has no effect on the conversation. ("completed"|"incomplete"|"in_progress")
- **role** (string (system)) (required): The role of the message sender. Always `system`. ("system")
- **content** (array (object)) (required): The content of the message.
  Array items:
    - **type** (string (input_text)): The content type. Always `input_text` for system messages. ("input_text")
    - **text** (string): The text content.

```

--------------------------------

### Schema: FineTuneSupervisedMethod

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Configuration for the supervised fine-tuning method.

```markdown
## Schema: FineTuneSupervisedMethod

Configuration for the supervised fine-tuning method.

**Type:** object

- **hyperparameters** (object): The hyperparameters used for the fine-tuning job.
  - **batch_size** (string (auto)) ("auto")
  - **learning_rate_multiplier** (string (auto)) ("auto")
  - **n_epochs** (string (auto)) ("auto")

```

--------------------------------

### GET /evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get an evaluation run output item by ID.


```markdown
### Parameters

- **eval_id** (string, path, required): The ID of the evaluation to retrieve runs for.
- **run_id** (string, path, required): The ID of the run to retrieve.
- **output_item_id** (string, path, required): The ID of the output item to retrieve.

### Responses

#### 200 - The evaluation run output item

**EvalRunOutputItem**
- **object** (string (eval.run.output_item)) (required): The type of the object. Always "eval.run.output_item". ("eval.run.output_item")
- **id** (string) (required): Unique identifier for the evaluation run output item.
- **run_id** (string) (required): The identifier of the evaluation run associated with this output item.
- **eval_id** (string) (required): The identifier of the evaluation group.
- **created_at** (integer) (required): Unix timestamp (in seconds) when the evaluation run was created.
- **status** (string) (required): The status of the evaluation run.
- **datasource_item_id** (integer) (required): The identifier for the data source item.
- **datasource_item** (object) (required): Details of the input data source item.
- **results** (array (object)) (required): A list of grader results for this output item.
  Array items:
    - **name** (string) (required): The name of the grader.
    - **type** (string): The grader type (for example, "string-check-grader").
    - **score** (number) (required): The numeric score produced by the grader.
    - **passed** (boolean) (required): Whether the grader considered the output a pass.
    - **sample** (object)
- **sample** (object) (required): A sample containing the input and output of the evaluation run.
  - **input** (array (object)) (required): An array of input messages.
    Array items:
      - **role** (string) (required): The role of the message sender (e.g., system, user, developer).
      - **content** (string) (required): The content of the message.
  - **output** (array (object)) (required): An array of output messages.
    Array items:
      - **role** (string): The role of the message (e.g. "system", "assistant", "user").
      - **content** (string): The content of the message.
  - **finish_reason** (string) (required): The reason why the sample generation was finished.
  - **model** (string) (required): The model used for generating the sample.
  - **usage** (object) (required): Token usage details for the sample.
    - **total_tokens** (integer) (required): The total number of tokens used.
    - **completion_tokens** (integer) (required): The number of completion tokens generated.
    - **prompt_tokens** (integer) (required): The number of prompt tokens used.
    - **cached_tokens** (integer) (required): The number of tokens retrieved from cache.
  - **error** (object) (required): An object representing an error response from the Eval API.

    - **code** (string) (required): The error code.
    - **message** (string) (required): The error message.
  - **temperature** (number) (required): The sampling temperature used.
  - **max_completion_tokens** (integer) (required): The maximum number of tokens allowed for completion.
  - **top_p** (number) (required): The top_p value used for sampling.
  - **seed** (integer) (required): The seed used for generating the sample.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}"
```

```

--------------------------------

### POST /vector_stores/{vector_store_id}/files

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create a vector store file by attaching a [File](https://platform.openai.com/docs/api-reference/files) to a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).

```markdown
### Parameters

- **vector_store_id** (string, path, required): The ID of the vector store for which to create a File.
 (example: "vs_abc123")

### Request Body

**Content-Type:** application/json

- **file_id** (string) (required): A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.
- **chunking_strategy** (object): The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.
  - **type** (string (auto)) (required): Always `auto`. ("auto")
- **attributes** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.


### Responses

#### 200 - OK

**VectorStoreFileObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (vector_store.file)) (required): The object type, which is always `vector_store.file`. ("vector_store.file")
- **usage_bytes** (integer) (required): The total vector store usage in bytes. Note that this may be different from the original file size.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store file was created.
- **vector_store_id** (string) (required): The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
- **status** (string (in_progress|completed|cancelled|failed)) (required): The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use. ("in_progress"|"completed"|"cancelled"|"failed")
- **last_error** (object) (required): The last error associated with this vector store file. Will be `null` if there are no errors.
  - **code** (string (server_error|unsupported_file|invalid_file)) (required): One of `server_error`, `unsupported_file`, or `invalid_file`. ("server_error"|"unsupported_file"|"invalid_file")
  - **message** (string) (required): A human-readable description of the error.
- **chunking_strategy** (object)
  - **type** (string (static)) (required): Always `static`. ("static")
  - **static** (object) (required)
    - **max_chunk_size_tokens** (integer) (required): The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.
    - **chunk_overlap_tokens** (integer) (required): The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

- **attributes** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.


### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/vector_stores/{vector_store_id}/files" \
  -H "Content-Type: application/json" \
  -d '{
  "file_id": "string",
  "chunking_strategy": {
    "type": "auto"
  },
  "attributes": "value"
}'
```

```

--------------------------------

### GET /conversations/{conversation_id}/items/{item_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get a single item from a conversation with the given IDs.

```markdown
### Parameters

- **conversation_id** (string, path, required): The ID of the conversation that contains the item. (example: "conv_123")
- **item_id** (string, path, required): The ID of the item to retrieve. (example: "msg_abc")
- **include** (array (IncludeEnum), query, optional): Additional fields to include in the response. See the `include`
parameter for [listing Conversation items above](https://platform.openai.com/docs/api-reference/conversations/list-items#conversations_list_items-include) for more information.


### Responses

#### 200 - OK

**ConversationItem**
- **type** (string (message)) (required): The type of the message. Always set to `message`. ("message")
- **id** (string) (required): The unique ID of the message.
- **status** (string (in_progress|completed|incomplete)) (required) ("in_progress"|"completed"|"incomplete")
- **role** (string (unknown|user|assistant|system|critic|discriminator|developer|tool)) (required) ("unknown"|"user"|"assistant"|"system"|"critic"|"discriminator"|"developer"|"tool")
- **content** (array (object)) (required): The content of the message
  Array items:
    - **type** (string (input_text)) (required): The type of the input item. Always `input_text`. ("input_text")
    - **text** (string) (required): The text input to the model.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/conversations/{conversation_id}/items/{item_id}?include=item1,item2"
```

```

--------------------------------

### GET /chat/completions/{completion_id}/messages

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get the messages in a stored chat completion. Only Chat Completions that
have been created with the `store` parameter set to `true` will be
returned.


```markdown
### Parameters

- **completion_id** (string, path, required): The ID of the chat completion to retrieve messages from.
- **after** (string, query, optional): Identifier for the last message from the previous pagination request.
- **limit** (integer, query, optional): Number of messages to retrieve.
- **order** (string (asc|desc), query, optional): Sort order for messages by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

### Responses

#### 200 - A list of messages

**ChatCompletionMessageList**
- **object** (string (list)) (required): The type of this object. It is always set to "list".
 ("list")
- **data** (array (object)) (required): An array of chat completion message objects.

  Array items:
    - **content** (string) (required): The contents of the message.
    - **refusal** (string) (required): The refusal message generated by the model.
    - **tool_calls** (array (object)): The tool calls generated by the model, such as function calls.
      Array items:
        - **id** (string) (required): The ID of the tool call.
        - **type** (string (function)) (required): The type of the tool. Currently, only `function` is supported. ("function")
        - **function** (object) (required): The function that the model called.
          - **name** (string) (required): The name of the function to call.
          - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
    - **annotations** (array (object)): Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

      Array items:
        - **type** (string (url_citation)) (required): The type of the URL citation. Always `url_citation`. ("url_citation")
        - **url_citation** (object) (required): A URL citation when using web search.
          - **end_index** (integer) (required): The index of the last character of the URL citation in the message.
          - **start_index** (integer) (required): The index of the first character of the URL citation in the message.
          - **url** (string) (required): The URL of the web resource.
          - **title** (string) (required): The title of the web resource.
    - **role** (string (assistant)) (required): The role of the author of this message. ("assistant")
    - **function_call** (object): Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.
      - **arguments** (string) (required): The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
      - **name** (string) (required): The name of the function to call.
    - **audio** (object): If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

      - **id** (string) (required): Unique identifier for this audio response.
      - **expires_at** (integer) (required): The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

      - **data** (string) (required): Base64 encoded audio bytes generated by the model, in the format
specified in the request.

      - **transcript** (string) (required): Transcript of the audio generated by the model.
    - **id** (string) (required): The identifier of the chat message.
    - **content_parts** (array (object)): If a content parts array was provided, this is an array of `text` and `image_url` parts.
Otherwise, null.

      Array items:
        - **type** (string (text)) (required): The type of the content part. ("text")
        - **text** (string) (required): The text content.
- **first_id** (string) (required): The identifier of the first chat message in the data array.
- **last_id** (string) (required): The identifier of the last chat message in the data array.
- **has_more** (boolean) (required): Indicates whether there are more chat messages available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/chat/completions/{completion_id}/messages?after=string&limit=20&order=asc"
```

```

--------------------------------

### POST /vector_stores/{vector_store_id}/file_batches

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create a vector store file batch.

```markdown
### Parameters

- **vector_store_id** (string, path, required): The ID of the vector store for which to create a File Batch.
 (example: "vs_abc123")

### Request Body

**Content-Type:** application/json

- **file_ids** (array (string)) (required): A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.
- **chunking_strategy** (object): The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.
  - **type** (string (auto)) (required): Always `auto`. ("auto")
- **attributes** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.


### Responses

#### 200 - OK

**VectorStoreFileBatchObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (vector_store.files_batch)) (required): The object type, which is always `vector_store.file_batch`. ("vector_store.files_batch")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store files batch was created.
- **vector_store_id** (string) (required): The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
- **status** (string (in_progress|completed|cancelled|failed)) (required): The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`. ("in_progress"|"completed"|"cancelled"|"failed")
- **file_counts** (object) (required)
  - **in_progress** (integer) (required): The number of files that are currently being processed.
  - **completed** (integer) (required): The number of files that have been processed.
  - **failed** (integer) (required): The number of files that have failed to process.
  - **cancelled** (integer) (required): The number of files that where cancelled.
  - **total** (integer) (required): The total number of files.

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/vector_stores/{vector_store_id}/file_batches" \
  -H "Content-Type: application/json" \
  -d '{
  "file_ids": [
    "string"
  ],
  "chunking_strategy": {
    "type": "auto"
  },
  "attributes": "value"
}'
```

```

--------------------------------

### GET /videos/{video_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieve a video

```markdown
### Parameters

- **video_id** (string, path, required): The identifier of the video to retrieve. (example: "video_123")

### Responses

#### 200 - Success

**VideoResource**
- **id** (string) (required): Unique identifier for the video job.
- **object** (string (video)) (required): The object type, which is always `video`. ("video")
- **model** (string (sora-2|sora-2-pro)) (required) ("sora-2"|"sora-2-pro")
- **status** (string (queued|in_progress|completed|failed)) (required) ("queued"|"in_progress"|"completed"|"failed")
- **progress** (integer) (required): Approximate completion percentage for the generation task.
- **created_at** (integer) (required): Unix timestamp (seconds) for when the job was created.
- **completed_at** (integer) (required): Unix timestamp (seconds) for when the job completed, if finished.
- **expires_at** (integer) (required): Unix timestamp (seconds) for when the downloadable assets expire, if set.
- **size** (string (720x1280|1280x720|1024x1792|1792x1024)) (required) ("720x1280"|"1280x720"|"1024x1792"|"1792x1024")
- **seconds** (string (4|8|12)) (required) ("4"|"8"|"12")
- **remixed_from_video_id** (string) (required): Identifier of the source video if this video is a remix.
- **error** (object) (required)
  - **code** (string) (required)
  - **message** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/videos/{video_id}"
```

```

--------------------------------

### GET /chatkit/threads

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List ChatKit threads

```markdown
### Parameters

- **limit** (integer, query, optional): Maximum number of thread items to return. Defaults to 20.
- **order** (OrderEnum, query, optional): Sort order for results by creation time. Defaults to `desc`.
- **after** (string, query, optional): List items created after this thread item ID. Defaults to null for the first page.
- **before** (string, query, optional): List items created before this thread item ID. Defaults to null for the newest results.
- **user** (string, query, optional): Filter threads that belong to this user identifier. Defaults to null to return all users.

### Responses

#### 200 - Success

**ThreadListResource**
- **object** (unknown) (required): The type of object returned, must be `list`.
- **data** (array (object)) (required): A list of items
  Array items:
    - **id** (string) (required): Identifier of the thread.
    - **object** (string (chatkit.thread)) (required): Type discriminator that is always `chatkit.thread`. ("chatkit.thread")
    - **created_at** (integer) (required): Unix timestamp (in seconds) for when the thread was created.
    - **title** (string) (required): Optional human-readable title for the thread. Defaults to null when no title has been generated.
    - **status** (object) (required): Indicates that a thread is active.
      - **type** (string (active)) (required): Status discriminator that is always `active`. ("active")
    - **user** (string) (required): Free-form string that identifies your end user who owns the thread.
- **first_id** (string) (required): The ID of the first item in the list.
- **last_id** (string) (required): The ID of the last item in the list.
- **has_more** (boolean) (required): Whether there are more items available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/chatkit/threads?limit=0&order=value&after=string&before=string&user=string"
```

```

--------------------------------

### Schema: FineTuneReinforcementMethod

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Configuration for the reinforcement fine-tuning method.

```markdown
## Schema: FineTuneReinforcementMethod

Configuration for the reinforcement fine-tuning method.

**Type:** object

- **grader** (object) (required): A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

  - **type** (string (string_check)) (required): The object type, which is always `string_check`. ("string_check")
  - **name** (string) (required): The name of the grader.
  - **input** (string) (required): The input text. This may include template strings.
  - **reference** (string) (required): The reference text. This may include template strings.
  - **operation** (string (eq|ne|like|ilike)) (required): The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`. ("eq"|"ne"|"like"|"ilike")
- **hyperparameters** (object): The hyperparameters used for the reinforcement fine-tuning job.
  - **batch_size** (string (auto)) ("auto")
  - **learning_rate_multiplier** (string (auto)) ("auto")
  - **n_epochs** (string (auto)) ("auto")
  - **reasoning_effort** (string (default|low|medium|high)): Level of reasoning effort.
 ("default"|"low"|"medium"|"high")
  - **compute_multiplier** (string (auto)) ("auto")
  - **eval_interval** (string (auto)) ("auto")
  - **eval_samples** (string (auto)) ("auto")

```

--------------------------------

### GET /organization/users

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Lists all of the users in the organization.

```markdown
### Parameters

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **emails** (array (string), query, optional): Filter by the email address of users.

### Responses

#### 200 - Users listed successfully.

**UserListResponse**
- **object** (string (list)) (required) ("list")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (organization.user)) (required): The object type, which is always `organization.user` ("organization.user")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **name** (string) (required): The name of the user
    - **email** (string) (required): The email address of the user
    - **role** (string (owner|reader)) (required): `owner` or `reader` ("owner"|"reader")
    - **added_at** (integer) (required): The Unix timestamp (in seconds) of when the user was added.
- **first_id** (string) (required)
- **last_id** (string) (required)
- **has_more** (boolean) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/users?limit=20&after=string&emails=item1,item2"
```

```

--------------------------------

### POST /realtime/calls

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create a new Realtime API call over WebRTC and receive the SDP answer needed
to complete the peer connection.

```markdown
### Request Body

**Content-Type:** multipart/form-data

- **sdp** (string) (required): WebRTC Session Description Protocol (SDP) offer generated by the caller.
- **session** (object): Realtime session object configuration.
  - **type** (string (realtime)) (required): The type of session to create. Always `realtime` for the Realtime API.
 ("realtime")
  - **output_modalities** (array (string (text|audio))): The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

  - **model** (string)
  - **instructions** (string): The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. "be extremely succinct", "act friendly", "here are examples of good responses") and on audio behavior (e.g. "talk quickly", "inject emotion into your voice", "laugh frequently"). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

  - **audio** (object): Configuration for input and output audio.

    - **input** (object)
      - **format** (object): The PCM audio format. Only a 24kHz sample rate is supported.
        - **type** (string (audio/pcm)): The audio format. Always `audio/pcm`. ("audio/pcm")
        - **rate** (integer): The sample rate of the audio. Always `24000`. ("24000")
      - **transcription** (object)
        - **model** (string (whisper-1|gpt-4o-mini-transcribe|gpt-4o-transcribe|gpt-4o-transcribe-diarize)): The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.
 ("whisper-1"|"gpt-4o-mini-transcribe"|"gpt-4o-transcribe"|"gpt-4o-transcribe-diarize")
        - **language** (string): The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

        - **prompt** (string): An optional text to guide the model's style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example "expect words related to technology".

      - **noise_reduction** (object): Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

        - **type** (string (near_field|far_field)): Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.
 ("near_field"|"far_field")
      - **turn_detection** (object): Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.
        - **type** (string) (required): Type of turn detection, `server_vad` to turn on simple Server VAD.

        - **threshold** (number): Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

        - **prefix_padding_ms** (integer): Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

        - **silence_duration_ms** (integer): Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

        - **create_response** (boolean): Whether or not to automatically generate a response when a VAD stop event occurs.

        - **interrupt_response** (boolean): Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

        - **idle_timeout_ms** (integer): Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response's audio has finished playing,
i.e. it's set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

    - **output** (object)
      - **format** (object): The PCM audio format. Only a 24kHz sample rate is supported.
      - **voice** (string)
      - **speed** (number): The speed of the model's spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it's
also possible to prompt the model to speak faster or slower.

  - **include** (array (string (item.input_audio_transcription.logprobs))): Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

  - **tracing** (string (auto)): Enables tracing and sets default values for tracing configuration options. Always `auto`.
 ("auto")
  - **tools** (array (object)): Tools available to the model.
    Array items:
      - **type** (string (function)): The type of the tool, i.e. `function`. ("function")
      - **name** (string): The name of the function.
      - **description** (string): The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

      - **parameters** (object): Parameters of the function in JSON Schema.
  - **tool_choice** (string (none|auto|required)): Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.
 ("none"|"auto"|"required")
  - **max_output_tokens** (integer)
  - **truncation** (string (auto|disabled)): The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit. ("auto"|"disabled")
  - **prompt** (object): Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

    - **id** (string) (required): The unique identifier of the prompt template to use.
    - **version** (string): Optional version of the prompt template.
    - **variables** (object): Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.


**Content-Type:** application/sdp


### Responses

#### 201 - Realtime call created successfully.


### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/realtime/calls" \
  -H "Content-Type: application/json" \
  -d '{
  "sdp": "string",
  "session": {
    "type": "realtime",
    "output_modalities": [
      "text"
    ],
    "model": "string",
    "instructions": "string",
    "audio": {
      "input": {
        "format": {
          "type": "audio/pcm",
          "rate": "0"
        },
        "transcription": {
          "model": "whisper-1",
          "language": "string",
          "prompt": "string"
        },
        "noise_reduction": {
          "type": "near_field"
        },
        "turn_detection": {
          "type": "server_vad",
          "threshold": "0",
          "prefix_padding_ms": "0",
          "silence_duration_ms": "0",
          "create_response": "true",
          "interrupt_response": "true",
          "idle_timeout_ms": "0"
        }
      },
      "output": {
        "format": {
          "type": "audio/pcm",
          "rate": "0"
        },
        "voice": "string",
        "speed": "1"
      }
    },
    "include": [
      "item.input_audio_transcription.logprobs"
    ],
    "tracing": "auto",
    "tools": [
      {
        "type": "function",
        "name": "string",
        "description": "string",
        "parameters": "value"
      }
    ],
    "tool_choice": "none",
    "max_output_tokens": "0",
    "truncation": "auto",
    "prompt": {
      "id": "string",
      "version": "string",
      "variables": "value"
    }
  }
}'
```

```

--------------------------------

### GET /organization/certificates

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List uploaded certificates for this organization.

```markdown
### Parameters

- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.


### Responses

#### 200 - Certificates listed successfully.

**ListCertificatesResponse**
- **data** (array (object)) (required)
  Array items:
    - **object** (string (certificate|organization.certificate|organization.project.certificate)) (required): The object type.

- If creating, updating, or getting a specific certificate, the object type is `certificate`.
- If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
- If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.
 ("certificate"|"organization.certificate"|"organization.project.certificate")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **name** (string) (required): The name of the certificate.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) of when the certificate was uploaded.
    - **certificate_details** (object) (required)
      - **valid_at** (integer): The Unix timestamp (in seconds) of when the certificate becomes valid.
      - **expires_at** (integer): The Unix timestamp (in seconds) of when the certificate expires.
      - **content** (string): The content of the certificate in PEM format.
    - **active** (boolean): Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.
- **first_id** (string) (example: "cert_abc")
- **last_id** (string) (example: "cert_abc")
- **has_more** (boolean) (required)
- **object** (string (list)) (required) ("list")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/certificates?limit=20&after=string&order=desc"
```

```

--------------------------------

### Schema: Audio content part

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).


```markdown
## Schema: Audio content part

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).


**Type:** object

- **type** (string (input_audio)) (required): The type of the content part. Always `input_audio`. ("input_audio")
- **input_audio** (object) (required)
  - **data** (string) (required): Base64 encoded audio data.
  - **format** (string (wav|mp3)) (required): The format of the encoded audio data. Currently supports "wav" and "mp3".
 ("wav"|"mp3")

```

--------------------------------

### POST /realtime/calls/{call_id}/accept

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Accept an incoming SIP call and configure the realtime session that will
handle it.

```markdown
### Parameters

- **call_id** (string, path, required): The identifier for the call provided in the
[`realtime.call.incoming`](https://platform.openai.com/docs/api-reference/webhook_events/realtime/call/incoming)
webhook.

### Request Body

**Content-Type:** application/json

- **type** (string (realtime)) (required): The type of session to create. Always `realtime` for the Realtime API.
 ("realtime")
- **output_modalities** (array (string (text|audio))): The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

- **model** (string)
- **instructions** (string): The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. "be extremely succinct", "act friendly", "here are examples of good responses") and on audio behavior (e.g. "talk quickly", "inject emotion into your voice", "laugh frequently"). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

- **audio** (object): Configuration for input and output audio.

  - **input** (object)
    - **format** (object): The PCM audio format. Only a 24kHz sample rate is supported.
      - **type** (string (audio/pcm)): The audio format. Always `audio/pcm`. ("audio/pcm")
      - **rate** (integer): The sample rate of the audio. Always `24000`. ("24000")
    - **transcription** (object)
      - **model** (string (whisper-1|gpt-4o-mini-transcribe|gpt-4o-transcribe|gpt-4o-transcribe-diarize)): The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.
 ("whisper-1"|"gpt-4o-mini-transcribe"|"gpt-4o-transcribe"|"gpt-4o-transcribe-diarize")
      - **language** (string): The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

      - **prompt** (string): An optional text to guide the model's style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example "expect words related to technology".

    - **noise_reduction** (object): Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

      - **type** (string (near_field|far_field)): Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.
 ("near_field"|"far_field")
    - **turn_detection** (object): Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.
      - **type** (string) (required): Type of turn detection, `server_vad` to turn on simple Server VAD.

      - **threshold** (number): Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

      - **prefix_padding_ms** (integer): Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

      - **silence_duration_ms** (integer): Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

      - **create_response** (boolean): Whether or not to automatically generate a response when a VAD stop event occurs.

      - **interrupt_response** (boolean): Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

      - **idle_timeout_ms** (integer): Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response's audio has finished playing,
i.e. it's set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

  - **output** (object)
    - **format** (object): The PCM audio format. Only a 24kHz sample rate is supported.
    - **voice** (string)
    - **speed** (number): The speed of the model's spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it's
also possible to prompt the model to speak faster or slower.

- **include** (array (string (item.input_audio_transcription.logprobs))): Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

- **tracing** (string (auto)): Enables tracing and sets default values for tracing configuration options. Always `auto`.
 ("auto")
- **tools** (array (object)): Tools available to the model.
  Array items:
    - **type** (string (function)): The type of the tool, i.e. `function`. ("function")
    - **name** (string): The name of the function.
    - **description** (string): The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

    - **parameters** (object): Parameters of the function in JSON Schema.
- **tool_choice** (string (none|auto|required)): Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.
 ("none"|"auto"|"required")
- **max_output_tokens** (integer)
- **truncation** (string (auto|disabled)): The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit. ("auto"|"disabled")
- **prompt** (object): Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

  - **id** (string) (required): The unique identifier of the prompt template to use.
  - **version** (string): Optional version of the prompt template.
  - **variables** (object): Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.


### Responses

#### 200 - Call accepted successfully.

Empty response body

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/realtime/calls/{call_id}/accept" \
  -H "Content-Type: application/json" \
  -d '{
  "type": "realtime",
  "output_modalities": [
    "text"
  ],
  "model": "string",
  "instructions": "string",
  "audio": {
    "input": {
      "format": {
        "type": "audio/pcm",
        "rate": "0"
      },
      "transcription": {
        "model": "whisper-1",
        "language": "string",
        "prompt": "string"
      },
      "noise_reduction": {
        "type": "near_field"
      },
      "turn_detection": {
        "type": "server_vad",
        "threshold": "0",
        "prefix_padding_ms": "0",
        "silence_duration_ms": "0",
        "create_response": "true",
        "interrupt_response": "true",
        "idle_timeout_ms": "0"
      }
    },
    "output": {
      "format": {
        "type": "audio/pcm",
        "rate": "0"
      },
      "voice": "string",
      "speed": "1"
    }
  },
  "include": [
    "item.input_audio_transcription.logprobs"
  ],
  "tracing": "auto",
  "tools": [
    {
      "type": "function",
      "name": "string",
      "description": "string",
      "parameters": "value"
    }
  ],
  "tool_choice": "none",
  "max_output_tokens": "0",
  "truncation": "auto",
  "prompt": {
    "id": "string",
    "version": "string",
    "variables": "value"
  }
}'
```

```

--------------------------------

### GET /vector_stores/{vector_store_id}/files

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of vector store files.

```markdown
### Parameters

- **vector_store_id** (string, path, required): The ID of the vector store that the files belong to.
- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **before** (string, query, optional): A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

- **filter** (string (in_progress|completed|failed|cancelled), query, optional): Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

### Responses

#### 200 - OK

**ListVectorStoreFilesResponse**

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/vector_stores/{vector_store_id}/files?limit=20&order=desc&after=string&before=string&filter=in_progress"
```

```

--------------------------------

### Schema: Computer use preview

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

```markdown
## Schema: Computer use preview

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

**Type:** object

- **type** (string (computer_use_preview)) (required): The type of the computer use tool. Always `computer_use_preview`. ("computer_use_preview")
- **environment** (string (windows|mac|linux|ubuntu|browser)) (required) ("windows"|"mac"|"linux"|"ubuntu"|"browser")
- **display_width** (integer) (required): The width of the computer display.
- **display_height** (integer) (required): The height of the computer display.

```

--------------------------------

### GET /vector_stores/{vector_store_id}/file_batches/{batch_id}/files

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of vector store files in a batch.

```markdown
### Parameters

- **vector_store_id** (string, path, required): The ID of the vector store that the files belong to.
- **batch_id** (string, path, required): The ID of the file batch that the files belong to.
- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- **before** (string, query, optional): A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

- **filter** (string (in_progress|completed|failed|cancelled), query, optional): Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

### Responses

#### 200 - OK

**ListVectorStoreFilesResponse**

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}/files?limit=20&order=desc&after=string&before=string&filter=in_progress"
```

```

--------------------------------

### GET /organization/admin_api_keys

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List organization API keys

```markdown
### Parameters

- **after** (string, query, optional)
- **order** (string (asc|desc), query, optional)
- **limit** (integer, query, optional)

### Responses

#### 200 - A list of organization API keys.

**ApiKeyList**
- **object** (string) (example: "list")
- **data** (array (object))
  Array items:
    - **object** (string) (required): The object type, which is always `organization.admin_api_key` (example: "organization.admin_api_key")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints (example: "key_abc")
    - **name** (string) (required): The name of the API key (example: "Administration Key")
    - **redacted_value** (string) (required): The redacted value of the API key (example: "sk-admin...def")
    - **value** (string): The value of the API key. Only shown on create. (example: "sk-admin-1234abcd")
    - **created_at** (integer (int64)) (required): The Unix timestamp (in seconds) of when the API key was created (example: 1711471533)
    - **last_used_at** (integer (int64)) (required): The Unix timestamp (in seconds) of when the API key was last used (example: 1711471534)
    - **owner** (object) (required)
      - **type** (string): Always `user` (example: "user")
      - **object** (string): The object type, which is always organization.user (example: "organization.user")
      - **id** (string): The identifier, which can be referenced in API endpoints (example: "sa_456")
      - **name** (string): The name of the user (example: "My Service Account")
      - **created_at** (integer (int64)): The Unix timestamp (in seconds) of when the user was created (example: 1711471533)
      - **role** (string): Always `owner` (example: "owner")
- **has_more** (boolean) (example: false)
- **first_id** (string) (example: "key_abc")
- **last_id** (string) (example: "key_xyz")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/admin_api_keys?after=string&order=asc&limit=20"
```

```

--------------------------------

### GET /assistants/{assistant_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves an assistant.

```markdown
### Parameters

- **assistant_id** (string, path, required): The ID of the assistant to retrieve.

### Responses

#### 200 - OK

**AssistantObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (assistant)) (required): The object type, which is always `assistant`. ("assistant")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the assistant was created.
- **name** (string) (required): The name of the assistant. The maximum length is 256 characters.

- **description** (string) (required): The description of the assistant. The maximum length is 512 characters.

- **model** (string) (required): ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

- **instructions** (string) (required): The system instructions that the assistant uses. The maximum length is 256,000 characters.

- **tools** (array (object)) (required): A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

  Array items:
    - **type** (string (code_interpreter)) (required): The type of tool being defined: `code_interpreter` ("code_interpreter")
- **tool_resources** (object): A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

  - **code_interpreter** (object)
    - **file_ids** (array (string)): A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

  - **file_search** (object)
    - **vector_store_ids** (array (string)): The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **temperature** (number): What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
 (example: 1)
- **top_p** (number): An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.
 (example: 1)
- **response_format** (string (auto)): `auto` is the default value
 ("auto")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/assistants/{assistant_id}"
```

```

--------------------------------

### Schema: CreateFineTuningCheckpointPermissionRequest

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Schema definition for CreateFineTuningCheckpointPermissionRequest

```markdown
## Schema: CreateFineTuningCheckpointPermissionRequest

Schema definition for CreateFineTuningCheckpointPermissionRequest

**Type:** object

- **project_ids** (array (string)) (required): The project identifiers to grant access to.

```

--------------------------------

### Schema: AssistantsApiResponseFormatOption

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.


```markdown
## Schema: AssistantsApiResponseFormatOption

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.


**Type:** object


```

--------------------------------

### GET /threads/{thread_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a thread.

```markdown
### Parameters

- **thread_id** (string, path, required): The ID of the thread to retrieve.

### Responses

#### 200 - OK

**ThreadObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (thread)) (required): The object type, which is always `thread`. ("thread")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the thread was created.
- **tool_resources** (object) (required): A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

  - **code_interpreter** (object)
    - **file_ids** (array (string)): A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

  - **file_search** (object)
    - **vector_store_ids** (array (string)): The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/threads/{thread_id}"
```

```

--------------------------------

### GET /containers/{container_id}/files

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List Container files

```markdown
### Parameters

- **container_id** (string, path, required)
- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **order** (string (asc|desc), query, optional): Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.


### Responses

#### 200 - Success

**ContainerFileListResource**
- **object** (unknown) (required): The type of object returned, must be 'list'.
- **data** (array (object)) (required): A list of container files.
  Array items:
    - **id** (string) (required): Unique identifier for the file.
    - **object** (string) (required): The type of this object (`container.file`).
    - **container_id** (string) (required): The container this file belongs to.
    - **created_at** (integer) (required): Unix timestamp (in seconds) when the file was created.
    - **bytes** (integer) (required): Size of the file in bytes.
    - **path** (string) (required): Path of the file in the container.
    - **source** (string) (required): Source of the file (e.g., `user`, `assistant`).
- **first_id** (string) (required): The ID of the first file in the list.
- **last_id** (string) (required): The ID of the last file in the list.
- **has_more** (boolean) (required): Whether there are more files available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/containers/{container_id}/files?limit=20&order=desc&after=string"
```

```

--------------------------------

### GET /organization/invites/{invite_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves an invite.

```markdown
### Parameters

- **invite_id** (string, path, required): The ID of the invite to retrieve.

### Responses

#### 200 - Invite retrieved successfully.

**Invite**
- **object** (string (organization.invite)) (required): The object type, which is always `organization.invite` ("organization.invite")
- **id** (string) (required): The identifier, which can be referenced in API endpoints
- **email** (string) (required): The email address of the individual to whom the invite was sent
- **role** (string (owner|reader)) (required): `owner` or `reader` ("owner"|"reader")
- **status** (string (accepted|expired|pending)) (required): `accepted`,`expired`, or `pending` ("accepted"|"expired"|"pending")
- **invited_at** (integer) (required): The Unix timestamp (in seconds) of when the invite was sent.
- **expires_at** (integer) (required): The Unix timestamp (in seconds) of when the invite expires.
- **accepted_at** (integer): The Unix timestamp (in seconds) of when the invite was accepted.
- **projects** (array (object)): The projects that were granted membership upon acceptance of the invite.
  Array items:
    - **id** (string): Project's public ID
    - **role** (string (member|owner)): Project membership role ("member"|"owner")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/invites/{invite_id}"
```

```

--------------------------------

### POST /organization/admin_api_keys

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create an organization admin API key

```markdown
### Request Body

**Content-Type:** application/json

- **name** (string) (required) (example: "New Admin Key")

### Responses

#### 200 - The newly created admin API key.

**AdminApiKey**
- **object** (string) (required): The object type, which is always `organization.admin_api_key` (example: "organization.admin_api_key")
- **id** (string) (required): The identifier, which can be referenced in API endpoints (example: "key_abc")
- **name** (string) (required): The name of the API key (example: "Administration Key")
- **redacted_value** (string) (required): The redacted value of the API key (example: "sk-admin...def")
- **value** (string): The value of the API key. Only shown on create. (example: "sk-admin-1234abcd")
- **created_at** (integer (int64)) (required): The Unix timestamp (in seconds) of when the API key was created (example: 1711471533)
- **last_used_at** (integer (int64)) (required): The Unix timestamp (in seconds) of when the API key was last used (example: 1711471534)
- **owner** (object) (required)
  - **type** (string): Always `user` (example: "user")
  - **object** (string): The object type, which is always organization.user (example: "organization.user")
  - **id** (string): The identifier, which can be referenced in API endpoints (example: "sa_456")
  - **name** (string): The name of the user (example: "My Service Account")
  - **created_at** (integer (int64)): The Unix timestamp (in seconds) of when the user was created (example: 1711471533)
  - **role** (string): Always `owner` (example: "owner")

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/organization/admin_api_keys" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "New Admin Key"
}'
```

```

--------------------------------

### GET /videos/{video_id}/content

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Download video content

```markdown
### Parameters

- **video_id** (string, path, required): The identifier of the video whose media to download. (example: "video_123")
- **variant** (VideoContentVariant, query, optional): Which downloadable asset to return. Defaults to the MP4 video.

### Responses

#### 200 - The video bytes or preview asset that matches the requested variant.




### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/videos/{video_id}/content?variant=value"
```

```

--------------------------------

### GET /containers/{container_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieve Container

```markdown
### Parameters

- **container_id** (string, path, required)

### Responses

#### 200 - Success

**ContainerResource**
- **id** (string) (required): Unique identifier for the container.
- **object** (string) (required): The type of this object.
- **name** (string) (required): Name of the container.
- **created_at** (integer) (required): Unix timestamp (in seconds) when the container was created.
- **status** (string) (required): Status of the container (e.g., active, deleted).
- **expires_after** (object): The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

  - **anchor** (string (last_active_at)): The reference point for the expiration. ("last_active_at")
  - **minutes** (integer): The number of minutes after the anchor before the container expires.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/containers/{container_id}"
```

```

--------------------------------

### POST /batches

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Creates and executes a batch from an uploaded file of requests

```markdown
### Request Body

**Content-Type:** application/json

- **input_file_id** (string) (required): The ID of an uploaded file that contains requests for the new batch.

See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

Your input file must be formatted as a [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 200 MB in size.

- **endpoint** (string (/v1/responses|/v1/chat/completions|/v1/embeddings|/v1/completions)) (required): The endpoint to be used for all requests in the batch. Currently `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, and `/v1/completions` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch. ("/v1/responses"|"/v1/chat/completions"|"/v1/embeddings"|"/v1/completions")
- **completion_window** (string (24h)) (required): The time frame within which the batch should be processed. Currently only `24h` is supported. ("24h")
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **output_expires_after** (object): The expiration policy for the output and/or error file that are generated for a batch.
  - **anchor** (string (created_at)) (required): Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. Note that the anchor is the file creation time, not the time the batch is created. ("created_at")
  - **seconds** (integer) (required): The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Responses

#### 200 - Batch created successfully.

**Batch**
- **id** (string) (required)
- **object** (string (batch)) (required): The object type, which is always `batch`. ("batch")
- **endpoint** (string) (required): The OpenAI API endpoint used by the batch.
- **model** (string): Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

- **errors** (object)
  - **object** (string): The object type, which is always `list`.
  - **data** (array (object))
    Array items:
      - **code** (string): An error code identifying the error type.
      - **message** (string): A human-readable message providing more details about the error.
      - **param** (string): The name of the parameter that caused the error, if applicable.
      - **line** (integer): The line number of the input file where the error occurred, if applicable.
- **input_file_id** (string) (required): The ID of the input file for the batch.
- **completion_window** (string) (required): The time frame within which the batch should be processed.
- **status** (string (validating|failed|in_progress|finalizing|completed|expired|cancelling|cancelled)) (required): The current status of the batch. ("validating"|"failed"|"in_progress"|"finalizing"|"completed"|"expired"|"cancelling"|"cancelled")
- **output_file_id** (string): The ID of the file containing the outputs of successfully executed requests.
- **error_file_id** (string): The ID of the file containing the outputs of requests with errors.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the batch was created.
- **in_progress_at** (integer): The Unix timestamp (in seconds) for when the batch started processing.
- **expires_at** (integer): The Unix timestamp (in seconds) for when the batch will expire.
- **finalizing_at** (integer): The Unix timestamp (in seconds) for when the batch started finalizing.
- **completed_at** (integer): The Unix timestamp (in seconds) for when the batch was completed.
- **failed_at** (integer): The Unix timestamp (in seconds) for when the batch failed.
- **expired_at** (integer): The Unix timestamp (in seconds) for when the batch expired.
- **cancelling_at** (integer): The Unix timestamp (in seconds) for when the batch started cancelling.
- **cancelled_at** (integer): The Unix timestamp (in seconds) for when the batch was cancelled.
- **request_counts** (object): The request counts for different statuses within the batch.
  - **total** (integer) (required): Total number of requests in the batch.
  - **completed** (integer) (required): Number of requests that have been completed successfully.
  - **failed** (integer) (required): Number of requests that have failed.
- **usage** (object): Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

  - **input_tokens** (integer) (required): The number of input tokens.
  - **input_tokens_details** (object) (required): A detailed breakdown of the input tokens.
    - **cached_tokens** (integer) (required): The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

  - **output_tokens** (integer) (required): The number of output tokens.
  - **output_tokens_details** (object) (required): A detailed breakdown of the output tokens.
    - **reasoning_tokens** (integer) (required): The number of reasoning tokens.
  - **total_tokens** (integer) (required): The total number of tokens used.
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/batches" \
  -H "Content-Type: application/json" \
  -d '{
  "input_file_id": "string",
  "endpoint": "/v1/responses",
  "completion_window": "24h",
  "metadata": "value",
  "output_expires_after": {
    "anchor": "created_at",
    "seconds": "0"
  }
}'
```

```

--------------------------------

### GET /batches/{batch_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a batch.

```markdown
### Parameters

- **batch_id** (string, path, required): The ID of the batch to retrieve.

### Responses

#### 200 - Batch retrieved successfully.

**Batch**
- **id** (string) (required)
- **object** (string (batch)) (required): The object type, which is always `batch`. ("batch")
- **endpoint** (string) (required): The OpenAI API endpoint used by the batch.
- **model** (string): Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model
guide](https://platform.openai.com/docs/models) to browse and compare available models.

- **errors** (object)
  - **object** (string): The object type, which is always `list`.
  - **data** (array (object))
    Array items:
      - **code** (string): An error code identifying the error type.
      - **message** (string): A human-readable message providing more details about the error.
      - **param** (string): The name of the parameter that caused the error, if applicable.
      - **line** (integer): The line number of the input file where the error occurred, if applicable.
- **input_file_id** (string) (required): The ID of the input file for the batch.
- **completion_window** (string) (required): The time frame within which the batch should be processed.
- **status** (string (validating|failed|in_progress|finalizing|completed|expired|cancelling|cancelled)) (required): The current status of the batch. ("validating"|"failed"|"in_progress"|"finalizing"|"completed"|"expired"|"cancelling"|"cancelled")
- **output_file_id** (string): The ID of the file containing the outputs of successfully executed requests.
- **error_file_id** (string): The ID of the file containing the outputs of requests with errors.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the batch was created.
- **in_progress_at** (integer): The Unix timestamp (in seconds) for when the batch started processing.
- **expires_at** (integer): The Unix timestamp (in seconds) for when the batch will expire.
- **finalizing_at** (integer): The Unix timestamp (in seconds) for when the batch started finalizing.
- **completed_at** (integer): The Unix timestamp (in seconds) for when the batch was completed.
- **failed_at** (integer): The Unix timestamp (in seconds) for when the batch failed.
- **expired_at** (integer): The Unix timestamp (in seconds) for when the batch expired.
- **cancelling_at** (integer): The Unix timestamp (in seconds) for when the batch started cancelling.
- **cancelled_at** (integer): The Unix timestamp (in seconds) for when the batch was cancelled.
- **request_counts** (object): The request counts for different statuses within the batch.
  - **total** (integer) (required): Total number of requests in the batch.
  - **completed** (integer) (required): Number of requests that have been completed successfully.
  - **failed** (integer) (required): Number of requests that have failed.
- **usage** (object): Represents token usage details including input tokens, output tokens, a
breakdown of output tokens, and the total tokens used. Only populated on
batches created after September 7, 2025.

  - **input_tokens** (integer) (required): The number of input tokens.
  - **input_tokens_details** (object) (required): A detailed breakdown of the input tokens.
    - **cached_tokens** (integer) (required): The number of tokens that were retrieved from the cache. [More on
prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

  - **output_tokens** (integer) (required): The number of output tokens.
  - **output_tokens_details** (object) (required): A detailed breakdown of the output tokens.
    - **reasoning_tokens** (integer) (required): The number of reasoning tokens.
  - **total_tokens** (integer) (required): The total number of tokens used.
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/batches/{batch_id}"
```

```

--------------------------------

### POST /containers

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create Container

```markdown
### Request Body

**Content-Type:** application/json

- **name** (string) (required): Name of the container to create.
- **file_ids** (array (string)): IDs of files to copy to the container.
- **expires_after** (object): Container expiration time in seconds relative to the 'anchor' time.
  - **anchor** (string (last_active_at)) (required): Time anchor for the expiration time. Currently only 'last_active_at' is supported. ("last_active_at")
  - **minutes** (integer) (required)

### Responses

#### 200 - Success

**ContainerResource**
- **id** (string) (required): Unique identifier for the container.
- **object** (string) (required): The type of this object.
- **name** (string) (required): Name of the container.
- **created_at** (integer) (required): Unix timestamp (in seconds) when the container was created.
- **status** (string) (required): Status of the container (e.g., active, deleted).
- **expires_after** (object): The container will expire after this time period.
The anchor is the reference point for the expiration.
The minutes is the number of minutes after the anchor before the container expires.

  - **anchor** (string (last_active_at)): The reference point for the expiration. ("last_active_at")
  - **minutes** (integer): The number of minutes after the anchor before the container expires.

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/containers" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "file_ids": [
    "string"
  ],
  "expires_after": {
    "anchor": "last_active_at",
    "minutes": "0"
  }
}'
```

```

--------------------------------

### GET /vector_stores/{vector_store_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a vector store.

```markdown
### Parameters

- **vector_store_id** (string, path, required): The ID of the vector store to retrieve.

### Responses

#### 200 - OK

**VectorStoreObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (vector_store)) (required): The object type, which is always `vector_store`. ("vector_store")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store was created.
- **name** (string) (required): The name of the vector store.
- **usage_bytes** (integer) (required): The total number of bytes used by the files in the vector store.
- **file_counts** (object) (required)
  - **in_progress** (integer) (required): The number of files that are currently being processed.
  - **completed** (integer) (required): The number of files that have been successfully processed.
  - **failed** (integer) (required): The number of files that have failed to process.
  - **cancelled** (integer) (required): The number of files that were cancelled.
  - **total** (integer) (required): The total number of files.
- **status** (string (expired|in_progress|completed)) (required): The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use. ("expired"|"in_progress"|"completed")
- **expires_after** (object): The expiration policy for a vector store.
  - **anchor** (string (last_active_at)) (required): Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`. ("last_active_at")
  - **days** (integer) (required): The number of days after the anchor time that the vector store will expire.
- **expires_at** (integer): The Unix timestamp (in seconds) for when the vector store will expire.
- **last_active_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store was last active.
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/vector_stores/{vector_store_id}"
```

```

--------------------------------

### Schema: FineTuneDPOMethod

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Configuration for the DPO fine-tuning method.

```markdown
## Schema: FineTuneDPOMethod

Configuration for the DPO fine-tuning method.

**Type:** object

- **hyperparameters** (object): The hyperparameters used for the DPO fine-tuning job.
  - **beta** (string (auto)) ("auto")
  - **batch_size** (string (auto)) ("auto")
  - **learning_rate_multiplier** (string (auto)) ("auto")
  - **n_epochs** (string (auto)) ("auto")

```

--------------------------------

### POST /responses/input_tokens

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Get input token counts

```markdown
### Request Body

**Content-Type:** application/json

- **model** (string): Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.
- **input** (string): A text input to the model, equivalent to a text input with the `user` role.
- **previous_response_id** (string): The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`. (example: "resp_123")
- **tools** (array (object)): An array of tools the model may call while generating a response. You can specify which tool to use by setting the `tool_choice` parameter.
  Array items:
    - **type** (string (function)) (required): The type of the function tool. Always `function`. ("function")
    - **name** (string) (required): The name of the function to call.
    - **description** (string): A description of the function. Used by the model to determine whether or not to call the function.
    - **parameters** (object) (required): A JSON schema object describing the parameters of the function.
    - **strict** (boolean) (required): Whether to enforce strict parameter validation. Default `true`.
- **text** (object): Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:
- [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

  - **format** (object): Default response format. Used to generate text responses.

    - **type** (string (text)) (required): The type of response format being defined. Always `text`. ("text")
  - **verbosity** (string (low|medium|high)): Constrains the verbosity of the model's response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.
 ("low"|"medium"|"high")
- **reasoning** (object): **gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

  - **effort** (string (minimal|low|medium|high)): Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `minimal`, `low`, `medium`, and `high`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
 ("minimal"|"low"|"medium"|"high")
  - **summary** (string (auto|concise|detailed)): A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is only supported for `computer-use-preview` models.
 ("auto"|"concise"|"detailed")
  - **generate_summary** (string (auto|concise|detailed)): **Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.
 ("auto"|"concise"|"detailed")
- **truncation** (string (auto|disabled)) ("auto"|"disabled")
- **instructions** (string): A system (or developer) message inserted into the model's context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.
- **conversation** (string): The unique ID of the conversation.

- **tool_choice** (string (none|auto|required)): Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.
 ("none"|"auto"|"required")
- **parallel_tool_calls** (boolean): Whether to allow the model to run tool calls in parallel.

**Content-Type:** application/x-www-form-urlencoded

- **model** (string): Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.
- **input** (string): A text input to the model, equivalent to a text input with the `user` role.
- **previous_response_id** (string): The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`. (example: "resp_123")
- **tools** (array (object)): An array of tools the model may call while generating a response. You can specify which tool to use by setting the `tool_choice` parameter.
  Array items:
    - **type** (string (function)) (required): The type of the function tool. Always `function`. ("function")
    - **name** (string) (required): The name of the function to call.
    - **description** (string): A description of the function. Used by the model to determine whether or not to call the function.
    - **parameters** (object) (required): A JSON schema object describing the parameters of the function.
    - **strict** (boolean) (required): Whether to enforce strict parameter validation. Default `true`.
- **text** (object): Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:
- [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

  - **format** (object): Default response format. Used to generate text responses.

    - **type** (string (text)) (required): The type of response format being defined. Always `text`. ("text")
  - **verbosity** (string (low|medium|high)): Constrains the verbosity of the model's response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.
 ("low"|"medium"|"high")
- **reasoning** (object): **gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

  - **effort** (string (minimal|low|medium|high)): Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `minimal`, `low`, `medium`, and `high`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

Note: The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
 ("minimal"|"low"|"medium"|"high")
  - **summary** (string (auto|concise|detailed)): A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is only supported for `computer-use-preview` models.
 ("auto"|"concise"|"detailed")
  - **generate_summary** (string (auto|concise|detailed)): **Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model's reasoning process.
One of `auto`, `concise`, or `detailed`.
 ("auto"|"concise"|"detailed")
- **truncation** (string (auto|disabled)) ("auto"|"disabled")
- **instructions** (string): A system (or developer) message inserted into the model's context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.
- **conversation** (string): The unique ID of the conversation.

- **tool_choice** (string (none|auto|required)): Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.
 ("none"|"auto"|"required")
- **parallel_tool_calls** (boolean): Whether to allow the model to run tool calls in parallel.

### Responses

#### 200 - Success

**TokenCountsResource**
- **object** (string (response.input_tokens)) (required) ("response.input_tokens")
- **input_tokens** (integer) (required)

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/responses/input_tokens" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "string",
  "input": "string",
  "previous_response_id": "resp_123",
  "tools": [
    {
      "type": "function",
      "name": "string",
      "description": "string",
      "parameters": "value",
      "strict": "true"
    }
  ],
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "medium"
  },
  "reasoning": {
    "effort": "medium",
    "summary": "auto",
    "generate_summary": "auto"
  },
  "truncation": "auto",
  "instructions": "string",
  "conversation": "string",
  "tool_choice": "none",
  "parallel_tool_calls": "true"
}'
```

```

--------------------------------

### Schema: FineTuneMethod

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

The method used for fine-tuning.

```markdown
## Schema: FineTuneMethod

The method used for fine-tuning.

**Type:** object

- **type** (string (supervised|dpo|reinforcement)) (required): The type of method. Is either `supervised`, `dpo`, or `reinforcement`. ("supervised"|"dpo"|"reinforcement")
- **supervised** (object): Configuration for the supervised fine-tuning method.
  - **hyperparameters** (object): The hyperparameters used for the fine-tuning job.
    - **batch_size** (string (auto)) ("auto")
    - **learning_rate_multiplier** (string (auto)) ("auto")
    - **n_epochs** (string (auto)) ("auto")
- **dpo** (object): Configuration for the DPO fine-tuning method.
  - **hyperparameters** (object): The hyperparameters used for the DPO fine-tuning job.
    - **beta** (string (auto)) ("auto")
    - **batch_size** (string (auto)) ("auto")
    - **learning_rate_multiplier** (string (auto)) ("auto")
    - **n_epochs** (string (auto)) ("auto")
- **reinforcement** (object): Configuration for the reinforcement fine-tuning method.
  - **grader** (object) (required): A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

    - **type** (string (string_check)) (required): The object type, which is always `string_check`. ("string_check")
    - **name** (string) (required): The name of the grader.
    - **input** (string) (required): The input text. This may include template strings.
    - **reference** (string) (required): The reference text. This may include template strings.
    - **operation** (string (eq|ne|like|ilike)) (required): The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`. ("eq"|"ne"|"like"|"ilike")
  - **hyperparameters** (object): The hyperparameters used for the reinforcement fine-tuning job.
    - **batch_size** (string (auto)) ("auto")
    - **learning_rate_multiplier** (string (auto)) ("auto")
    - **n_epochs** (string (auto)) ("auto")
    - **reasoning_effort** (string (default|low|medium|high)): Level of reasoning effort.
 ("default"|"low"|"medium"|"high")
    - **compute_multiplier** (string (auto)) ("auto")
    - **eval_interval** (string (auto)) ("auto")
    - **eval_samples** (string (auto)) ("auto")

```

--------------------------------

### Schema: RealtimeBetaResponse

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

The response resource.

```markdown
## Schema: RealtimeBetaResponse

The response resource.

**Type:** object

- **id** (string): The unique ID of the response.
- **object** (unknown): The object type, must be `realtime.response`.
- **status** (string (completed|cancelled|failed|incomplete|in_progress)): The final status of the response (`completed`, `cancelled`, `failed`, or 
`incomplete`, `in_progress`).
 ("completed"|"cancelled"|"failed"|"incomplete"|"in_progress")
- **status_details** (object): Additional details about the status.
  - **type** (string (completed|cancelled|incomplete|failed)): The type of error that caused the response to fail, corresponding 
with the `status` field (`completed`, `cancelled`, `incomplete`, 
`failed`).
 ("completed"|"cancelled"|"incomplete"|"failed")
  - **reason** (string (turn_detected|client_cancelled|max_output_tokens|content_filter)): The reason the Response did not complete. For a `cancelled` Response, 
one of `turn_detected` (the server VAD detected a new start of speech) 
or `client_cancelled` (the client sent a cancel event). For an 
`incomplete` Response, one of `max_output_tokens` or `content_filter` 
(the server-side safety filter activated and cut off the response).
 ("turn_detected"|"client_cancelled"|"max_output_tokens"|"content_filter")
  - **error** (object): A description of the error that caused the response to fail, 
populated when the `status` is `failed`.

    - **type** (string): The type of error.
    - **code** (string): Error code, if any.
- **output** (array (object)): The list of output items generated by the response.
  Array items:
    - **id** (string): The unique ID of the item. This may be provided by the client or generated by the server.
    - **object** (string (realtime.item)): Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item. ("realtime.item")
    - **type** (string (message)) (required): The type of the item. Always `message`. ("message")
    - **status** (string (completed|incomplete|in_progress)): The status of the item. Has no effect on the conversation. ("completed"|"incomplete"|"in_progress")
    - **role** (string (system)) (required): The role of the message sender. Always `system`. ("system")
    - **content** (array (object)) (required): The content of the message.
      Array items:
        - **type** (string (input_text)): The content type. Always `input_text` for system messages. ("input_text")
        - **text** (string): The text content.
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **usage** (object): Usage statistics for the Response, this will correspond to billing. A 
Realtime API session will maintain a conversation context and append new 
Items to the Conversation, thus output from previous turns (text and 
audio tokens) will become the input for later turns.

  - **total_tokens** (integer): The total number of tokens in the Response including input and output 
text and audio tokens.

  - **input_tokens** (integer): The number of input tokens used in the Response, including text and 
audio tokens.

  - **output_tokens** (integer): The number of output tokens sent in the Response, including text and 
audio tokens.

  - **input_token_details** (object): Details about the input tokens used in the Response.
    - **cached_tokens** (integer): The number of cached tokens used as input for the Response.
    - **text_tokens** (integer): The number of text tokens used as input for the Response.
    - **image_tokens** (integer): The number of image tokens used as input for the Response.
    - **audio_tokens** (integer): The number of audio tokens used as input for the Response.
    - **cached_tokens_details** (object): Details about the cached tokens used as input for the Response.
      - **text_tokens** (integer): The number of cached text tokens used as input for the Response.
      - **image_tokens** (integer): The number of cached image tokens used as input for the Response.
      - **audio_tokens** (integer): The number of cached audio tokens used as input for the Response.
  - **output_token_details** (object): Details about the output tokens used in the Response.
    - **text_tokens** (integer): The number of text tokens used in the Response.
    - **audio_tokens** (integer): The number of audio tokens used in the Response.
- **conversation_id** (string): Which conversation the response is added to, determined by the `conversation`
field in the `response.create` event. If `auto`, the response will be added to
the default conversation and the value of `conversation_id` will be an id like
`conv_1234`. If `none`, the response will not be added to any conversation and
the value of `conversation_id` will be `null`. If responses are being triggered
by server VAD, the response will be added to the default conversation, thus
the `conversation_id` will be an id like `conv_1234`.

- **voice** (string)
- **modalities** (array (string (text|audio))): The set of modalities the model used to respond. If there are multiple modalities,
the model will pick one, for example if `modalities` is `["text", "audio"]`, the model
could be responding in either text or audio.

- **output_audio_format** (string (pcm16|g711_ulaw|g711_alaw)): The format of output audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`.
 ("pcm16"|"g711_ulaw"|"g711_alaw")
- **temperature** (number): Sampling temperature for the model, limited to [0.6, 1.2]. Defaults to 0.8.

- **max_output_tokens** (integer)

```

--------------------------------

### Schema: RealtimeServerEventConversationItemInputAudioTranscriptionCompleted

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (when VAD is enabled). Transcription runs
asynchronously with Response creation, so this event may come before or after
the Response events.

Realtime API models accept audio natively, and thus input transcription is a
separate process run on a separate ASR (Automatic Speech Recognition) model.
The transcript may diverge somewhat from the model's interpretation, and
should be treated as a rough guide.


```markdown
## Schema: RealtimeServerEventConversationItemInputAudioTranscriptionCompleted

This event is the output of audio transcription for user audio written to the
user audio buffer. Transcription begins when the input audio buffer is
committed by the client or server (when VAD is enabled). Transcription runs
asynchronously with Response creation, so this event may come before or after
the Response events.

Realtime API models accept audio natively, and thus input transcription is a
separate process run on a separate ASR (Automatic Speech Recognition) model.
The transcript may diverge somewhat from the model's interpretation, and
should be treated as a rough guide.


**Type:** object

- **event_id** (string) (required): The unique ID of the server event.
- **type** (string (conversation.item.input_audio_transcription.completed)) (required): The event type, must be
`conversation.item.input_audio_transcription.completed`.
 ("conversation.item.input_audio_transcription.completed")
- **item_id** (string) (required): The ID of the item containing the audio that is being transcribed.
- **content_index** (integer) (required): The index of the content part containing the audio.
- **transcript** (string) (required): The transcribed text.
- **logprobs** (array (object)): The log probabilities of the transcription.
  Array items:
    - **token** (string) (required): The token that was used to generate the log probability.

    - **logprob** (number) (required): The log probability of the token.

    - **bytes** (array (integer)) (required): The bytes that were used to generate the log probability.

- **usage** (object) (required): Usage statistics for models billed by token usage.
  - **type** (string (tokens)) (required): The type of the usage object. Always `tokens` for this variant. ("tokens")
  - **input_tokens** (integer) (required): Number of input tokens billed for this request.
  - **input_token_details** (object): Details about the input tokens billed for this request.
    - **text_tokens** (integer): Number of text tokens billed for this request.
    - **audio_tokens** (integer): Number of audio tokens billed for this request.
  - **output_tokens** (integer) (required): Number of output tokens generated.
  - **total_tokens** (integer) (required): Total number of tokens used (input + output).

```

--------------------------------

### GET /chatkit/threads/{thread_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieve a ChatKit thread

```markdown
### Parameters

- **thread_id** (string, path, required): Identifier of the ChatKit thread to retrieve. (example: "cthr_123")

### Responses

#### 200 - Success

**ThreadResource**
- **id** (string) (required): Identifier of the thread.
- **object** (string (chatkit.thread)) (required): Type discriminator that is always `chatkit.thread`. ("chatkit.thread")
- **created_at** (integer) (required): Unix timestamp (in seconds) for when the thread was created.
- **title** (string) (required): Optional human-readable title for the thread. Defaults to null when no title has been generated.
- **status** (object) (required): Indicates that a thread is active.
  - **type** (string (active)) (required): Status discriminator that is always `active`. ("active")
- **user** (string) (required): Free-form string that identifies your end user who owns the thread.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/chatkit/threads/{thread_id}"
```

```

--------------------------------

### API Overview: OpenAI API

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

```yaml
# OpenAI API
# Version: 2.3.0

The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

# Base URL: https://api.openai.com/v1
```

--------------------------------

### GET /vector_stores/{vector_store_id}/files/{file_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a vector store file.

```markdown
### Parameters

- **vector_store_id** (string, path, required): The ID of the vector store that the file belongs to. (example: "vs_abc123")
- **file_id** (string, path, required): The ID of the file being retrieved. (example: "file-abc123")

### Responses

#### 200 - OK

**VectorStoreFileObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (vector_store.file)) (required): The object type, which is always `vector_store.file`. ("vector_store.file")
- **usage_bytes** (integer) (required): The total vector store usage in bytes. Note that this may be different from the original file size.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store file was created.
- **vector_store_id** (string) (required): The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
- **status** (string (in_progress|completed|cancelled|failed)) (required): The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use. ("in_progress"|"completed"|"cancelled"|"failed")
- **last_error** (object) (required): The last error associated with this vector store file. Will be `null` if there are no errors.
  - **code** (string (server_error|unsupported_file|invalid_file)) (required): One of `server_error`, `unsupported_file`, or `invalid_file`. ("server_error"|"unsupported_file"|"invalid_file")
  - **message** (string) (required): A human-readable description of the error.
- **chunking_strategy** (object)
  - **type** (string (static)) (required): Always `static`. ("static")
  - **static** (object) (required)
    - **max_chunk_size_tokens** (integer) (required): The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.
    - **chunk_overlap_tokens** (integer) (required): The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

- **attributes** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/vector_stores/{vector_store_id}/files/{file_id}"
```

```

--------------------------------

### Schema: RealtimeBetaServerEventMCPListToolsCompleted

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returned when listing MCP tools has completed for an item.

```markdown
## Schema: RealtimeBetaServerEventMCPListToolsCompleted

Returned when listing MCP tools has completed for an item.

**Type:** object

- **event_id** (string) (required): The unique ID of the server event.
- **type** (unknown) (required): The event type, must be `mcp_list_tools.completed`.
- **item_id** (string) (required): The ID of the MCP list tools item.

```

--------------------------------

### GET /vector_stores/{vector_store_id}/file_batches/{batch_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a vector store file batch.

```markdown
### Parameters

- **vector_store_id** (string, path, required): The ID of the vector store that the file batch belongs to. (example: "vs_abc123")
- **batch_id** (string, path, required): The ID of the file batch being retrieved. (example: "vsfb_abc123")

### Responses

#### 200 - OK

**VectorStoreFileBatchObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (vector_store.files_batch)) (required): The object type, which is always `vector_store.file_batch`. ("vector_store.files_batch")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the vector store files batch was created.
- **vector_store_id** (string) (required): The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
- **status** (string (in_progress|completed|cancelled|failed)) (required): The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`. ("in_progress"|"completed"|"cancelled"|"failed")
- **file_counts** (object) (required)
  - **in_progress** (integer) (required): The number of files that are currently being processed.
  - **completed** (integer) (required): The number of files that have been processed.
  - **failed** (integer) (required): The number of files that have failed to process.
  - **cancelled** (integer) (required): The number of files that where cancelled.
  - **total** (integer) (required): The total number of files.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/vector_stores/{vector_store_id}/file_batches/{batch_id}"
```

```

--------------------------------

### GET /organization/users/{user_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a user by their identifier.

```markdown
### Parameters

- **user_id** (string, path, required): The ID of the user.

### Responses

#### 200 - User retrieved successfully.

**User**
- **object** (string (organization.user)) (required): The object type, which is always `organization.user` ("organization.user")
- **id** (string) (required): The identifier, which can be referenced in API endpoints
- **name** (string) (required): The name of the user
- **email** (string) (required): The email address of the user
- **role** (string (owner|reader)) (required): `owner` or `reader` ("owner"|"reader")
- **added_at** (integer) (required): The Unix timestamp (in seconds) of when the user was added.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/users/{user_id}"
```

```

--------------------------------

### POST /evals/{eval_id}/runs

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Kicks off a new run for a given evaluation, specifying the data source, and what model configuration to use to test. The datasource will be validated against the schema specified in the config of the evaluation.


```markdown
### Parameters

- **eval_id** (string, path, required): The ID of the evaluation to create a run for.

### Request Body

**Content-Type:** application/json

- **name** (string): The name of the run.
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **data_source** (object) (required): A JsonlRunDataSource object with that specifies a JSONL file that matches the eval 

  - **type** (string (jsonl)) (required): The type of data source. Always `jsonl`. ("jsonl")
  - **source** (object) (required)
    - **type** (string (file_content)) (required): The type of jsonl source. Always `file_content`. ("file_content")
    - **content** (array (object)) (required): The content of the jsonl file.
      Array items:
        - **item** (object) (required)
        - **sample** (object)

### Responses

#### 201 - Successfully created a run for the evaluation

**EvalRun**
- **object** (string (eval.run)) (required): The type of the object. Always "eval.run". ("eval.run")
- **id** (string) (required): Unique identifier for the evaluation run.
- **eval_id** (string) (required): The identifier of the associated evaluation.
- **status** (string) (required): The status of the evaluation run.
- **model** (string) (required): The model that is evaluated, if applicable.
- **name** (string) (required): The name of the evaluation run.
- **created_at** (integer) (required): Unix timestamp (in seconds) when the evaluation run was created.
- **report_url** (string) (required): The URL to the rendered evaluation run report on the UI dashboard.
- **result_counts** (object) (required): Counters summarizing the outcomes of the evaluation run.
  - **total** (integer) (required): Total number of executed output items.
  - **errored** (integer) (required): Number of output items that resulted in an error.
  - **failed** (integer) (required): Number of output items that failed to pass the evaluation.
  - **passed** (integer) (required): Number of output items that passed the evaluation.
- **per_model_usage** (array (object)) (required): Usage statistics for each model during the evaluation run.
  Array items:
    - **model_name** (string) (required): The name of the model.
    - **invocation_count** (integer) (required): The number of invocations.
    - **prompt_tokens** (integer) (required): The number of prompt tokens used.
    - **completion_tokens** (integer) (required): The number of completion tokens generated.
    - **total_tokens** (integer) (required): The total number of tokens used.
    - **cached_tokens** (integer) (required): The number of tokens retrieved from cache.
- **per_testing_criteria_results** (array (object)) (required): Results per testing criteria applied during the evaluation run.
  Array items:
    - **testing_criteria** (string) (required): A description of the testing criteria.
    - **passed** (integer) (required): Number of tests passed for this criteria.
    - **failed** (integer) (required): Number of tests failed for this criteria.
- **data_source** (object) (required): A JsonlRunDataSource object with that specifies a JSONL file that matches the eval 

  - **type** (string (jsonl)) (required): The type of data source. Always `jsonl`. ("jsonl")
  - **source** (object) (required)
    - **type** (string (file_content)) (required): The type of jsonl source. Always `file_content`. ("file_content")
    - **content** (array (object)) (required): The content of the jsonl file.
      Array items:
        - **item** (object) (required)
        - **sample** (object)
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **error** (object) (required): An object representing an error response from the Eval API.

  - **code** (string) (required): The error code.
  - **message** (string) (required): The error message.

#### 400 - Bad request (for example, missing eval object)

**Error**
- **code** (string) (required)
- **message** (string) (required)
- **param** (string) (required)
- **type** (string) (required)

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/evals/{eval_id}/runs" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "metadata": "value",
  "data_source": {
    "type": "jsonl",
    "source": {
      "type": "file_content",
      "content": [
        {
          "item": "value",
          "sample": "value"
        }
      ]
    }
  }
}'
```

```

--------------------------------

### POST /evals

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create the structure of an evaluation that can be used to test a model's performance.
An evaluation is a set of testing criteria and the config for a data source, which dictates the schema of the data used in the evaluation. After creating an evaluation, you can run it on different models and model parameters. We support several types of graders and datasources.
For more information, see the [Evals guide](https://platform.openai.com/docs/guides/evals).


```markdown
### Request Body

**Content-Type:** application/json

- **name** (string): The name of the evaluation.
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **data_source_config** (object) (required): A CustomDataSourceConfig object that defines the schema for the data source used for the evaluation runs.
This schema is used to define the shape of the data that will be:
- Used to define your testing criteria and
- What data is required when creating a run

  - **type** (string (custom)) (required): The type of data source. Always `custom`. ("custom")
  - **item_schema** (object) (required): The json schema for each row in the data source.
  - **include_sample_schema** (boolean): Whether the eval should expect you to populate the sample namespace (ie, by generating responses off of your data source)
- **testing_criteria** (array (object)) (required): A list of graders for all eval runs in this group. Graders can reference variables in the data source using double curly braces notation, like `{{item.variable_name}}`. To reference the model's output, use the `sample` namespace (ie, `{{sample.output_text}}`).
  Array items:
    - **type** (string (label_model)) (required): The object type, which is always `label_model`. ("label_model")
    - **name** (string) (required): The name of the grader.
    - **model** (string) (required): The model to use for the evaluation. Must support structured outputs.
    - **input** (array (object)) (required): A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.
      Array items:
        - **role** (string) (required): The role of the message (e.g. "system", "assistant", "user").
        - **content** (string) (required): The content of the message.
    - **labels** (array (string)) (required): The labels to classify to each item in the evaluation.
    - **passing_labels** (array (string)) (required): The labels that indicate a passing result. Must be a subset of labels.

### Responses

#### 201 - OK

**Eval**
- **object** (string (eval)) (required): The object type. ("eval")
- **id** (string) (required): Unique identifier for the evaluation.
- **name** (string) (required): The name of the evaluation. (example: "Chatbot effectiveness Evaluation")
- **data_source_config** (object) (required): A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:
- Used to define your testing criteria and
- What data is required when creating a run

  - **type** (string (custom)) (required): The type of data source. Always `custom`. ("custom")
  - **schema** (object) (required): The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

- **testing_criteria** (array (object)) (required): A list of testing criteria.
  Array items:
    - **type** (string (label_model)) (required): The object type, which is always `label_model`. ("label_model")
    - **name** (string) (required): The name of the grader.
    - **model** (string) (required): The model to use for the evaluation. Must support structured outputs.
    - **input** (array (object)) (required)
      Array items:
        - **role** (string (user|assistant|system|developer)) (required): The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.
 ("user"|"assistant"|"system"|"developer")
        - **content** (string) (required): A text input to the model.

        - **type** (string (message)): The type of the message input. Always `message`.
 ("message")
    - **labels** (array (string)) (required): The labels to assign to each item in the evaluation.
    - **passing_labels** (array (string)) (required): The labels that indicate a passing result. Must be a subset of labels.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the eval was created.
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/evals" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "metadata": "value",
  "data_source_config": {
    "type": "custom",
    "item_schema": "value",
    "include_sample_schema": "false"
  },
  "testing_criteria": [
    {
      "type": "label_model",
      "name": "string",
      "model": "string",
      "input": [
        {
          "role": "string",
          "content": "string"
        }
      ],
      "labels": [
        "string"
      ],
      "passing_labels": [
        "string"
      ]
    }
  ]
}'
```

```

--------------------------------

### POST /threads

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Create a thread.

```markdown
### Request Body

**Content-Type:** application/json

- **messages** (array (object)): A list of [messages](https://platform.openai.com/docs/api-reference/messages) to start the thread with.
  Array items:
    - **role** (string (user|assistant)) (required): The role of the entity that is creating the message. Allowed values include:
- `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
- `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.
 ("user"|"assistant")
    - **content** (string) (required): The text contents of the message.
    - **attachments** (array (object)): A list of files attached to the message, and the tools they should be added to.
      Array items:
        - **file_id** (string): The ID of the file to attach to the message.
        - **tools** (array (object)): The tools to add this file to.
          Array items:
            - **type** (string (code_interpreter)) (required): The type of tool being defined: `code_interpreter` ("code_interpreter")
    - **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **tool_resources** (object): A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

  - **code_interpreter** (object)
    - **file_ids** (array (string)): A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

  - **file_search** (unknown)
- **metadata** (object): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Responses

#### 200 - OK

**ThreadObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (thread)) (required): The object type, which is always `thread`. ("thread")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the thread was created.
- **tool_resources** (object) (required): A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

  - **code_interpreter** (object)
    - **file_ids** (array (string)): A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

  - **file_search** (object)
    - **vector_store_ids** (array (string)): The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/threads" \
  -H "Content-Type: application/json" \
  -d '{
  "messages": [
    {
      "role": "user",
      "content": "string",
      "attachments": [
        {
          "file_id": "string",
          "tools": [
            {
              "type": "code_interpreter"
            }
          ]
        }
      ],
      "metadata": "value"
    }
  ],
  "tool_resources": {
    "code_interpreter": {
      "file_ids": [
        "string"
      ]
    },
    "file_search": "value"
  },
  "metadata": "value"
}'
```

```

--------------------------------

### GET /organization/projects/{project_id}/users

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of users in the project.

```markdown
### Parameters

- **project_id** (string, path, required): The ID of the project.
- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.


### Responses

#### 200 - Project users listed successfully.

**ProjectUserListResponse**
- **object** (string) (required)
- **data** (array (object)) (required)
  Array items:
    - **object** (string (organization.project.user)) (required): The object type, which is always `organization.project.user` ("organization.project.user")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **name** (string) (required): The name of the user
    - **email** (string) (required): The email address of the user
    - **role** (string (owner|member)) (required): `owner` or `member` ("owner"|"member")
    - **added_at** (integer) (required): The Unix timestamp (in seconds) of when the project was added.
- **first_id** (string) (required)
- **last_id** (string) (required)
- **has_more** (boolean) (required)

#### 400 - Error response when project is archived.

**ErrorResponse**
- **error** (object) (required)
  - **code** (string) (required)
  - **message** (string) (required)
  - **param** (string) (required)
  - **type** (string) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/projects/{project_id}/users?limit=20&after=string"
```

```

--------------------------------

### GET /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.


```markdown
### Parameters

- **fine_tuned_model_checkpoint** (string, path, required): The ID of the fine-tuned model checkpoint to get permissions for.
 (example: "ft-AF1WoRqd3aJAHsqc9NY7iL8F")
- **project_id** (string, query, optional): The ID of the project to get permissions for.
- **after** (string, query, optional): Identifier for the last permission ID from the previous pagination request.
- **limit** (integer, query, optional): Number of permissions to retrieve.
- **order** (string (ascending|descending), query, optional): The order in which to retrieve permissions.

### Responses

#### 200 - OK

**ListFineTuningCheckpointPermissionResponse**
- **data** (array (object)) (required)
  Array items:
    - **id** (string) (required): The permission identifier, which can be referenced in the API endpoints.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the permission was created.
    - **project_id** (string) (required): The project identifier that the permission is for.
    - **object** (string (checkpoint.permission)) (required): The object type, which is always "checkpoint.permission". ("checkpoint.permission")
- **object** (string (list)) (required) ("list")
- **first_id** (string)
- **last_id** (string)
- **has_more** (boolean) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions?project_id=string&after=string&limit=10&order=descending"
```

```

--------------------------------

### GET /files/{file_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns information about a specific file.

```markdown
### Parameters

- **file_id** (string, path, required): The ID of the file to use for this request.

### Responses

#### 200 - OK

**OpenAIFile**

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/files/{file_id}"
```

```

--------------------------------

### Schema: FineTuningJobEvent

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Fine-tuning job event object

```markdown
## Schema: FineTuningJobEvent

Fine-tuning job event object

**Type:** object

- **object** (string (fine_tuning.job.event)) (required): The object type, which is always "fine_tuning.job.event". ("fine_tuning.job.event")
- **id** (string) (required): The object identifier.
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the fine-tuning job was created.
- **level** (string (info|warn|error)) (required): The log level of the event. ("info"|"warn"|"error")
- **message** (string) (required): The message of the event.
- **type** (string (message|metrics)): The type of event. ("message"|"metrics")
- **data** (object): The data associated with the event.

```

--------------------------------

### Schema: Fine-Tuning Job Integration

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Schema definition for FineTuningIntegration

```markdown
## Schema: Fine-Tuning Job Integration

Schema definition for FineTuningIntegration

**Type:** object

- **type** (string (wandb)) (required): The type of the integration being enabled for the fine-tuning job ("wandb")
- **wandb** (object) (required): The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

  - **project** (string) (required): The name of the project that the new run will be created under.
 (example: "my-wandb-project")
  - **name** (string): A display name to set for the run. If not set, we will use the Job ID as the name.

  - **entity** (string): The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

  - **tags** (array (string)): A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".


```

--------------------------------

### GET /threads/{thread_id}/runs/{run_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a run.

```markdown
### Parameters

- **thread_id** (string, path, required): The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.
- **run_id** (string, path, required): The ID of the run to retrieve.

### Responses

#### 200 - OK

**RunObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (thread.run)) (required): The object type, which is always `thread.run`. ("thread.run")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the run was created.
- **thread_id** (string) (required): The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.
- **assistant_id** (string) (required): The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.
- **status** (string (queued|in_progress|requires_action|cancelling|cancelled|failed|completed|incomplete|expired)) (required): The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`. ("queued"|"in_progress"|"requires_action"|"cancelling"|"cancelled"|"failed"|"completed"|"incomplete"|"expired")
- **required_action** (object) (required): Details on the action required to continue the run. Will be `null` if no action is required.
  - **type** (string (submit_tool_outputs)) (required): For now, this is always `submit_tool_outputs`. ("submit_tool_outputs")
  - **submit_tool_outputs** (object) (required): Details on the tool outputs needed for this run to continue.
    - **tool_calls** (array (object)) (required): A list of the relevant tool calls.
      Array items:
        - **id** (string) (required): The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.
        - **type** (string (function)) (required): The type of tool call the output is required for. For now, this is always `function`. ("function")
        - **function** (object) (required): The function definition.
          - **name** (string) (required): The name of the function.
          - **arguments** (string) (required): The arguments that the model expects you to pass to the function.
- **last_error** (object) (required): The last error associated with this run. Will be `null` if there are no errors.
  - **code** (string (server_error|rate_limit_exceeded|invalid_prompt)) (required): One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`. ("server_error"|"rate_limit_exceeded"|"invalid_prompt")
  - **message** (string) (required): A human-readable description of the error.
- **expires_at** (integer) (required): The Unix timestamp (in seconds) for when the run will expire.
- **started_at** (integer) (required): The Unix timestamp (in seconds) for when the run was started.
- **cancelled_at** (integer) (required): The Unix timestamp (in seconds) for when the run was cancelled.
- **failed_at** (integer) (required): The Unix timestamp (in seconds) for when the run failed.
- **completed_at** (integer) (required): The Unix timestamp (in seconds) for when the run was completed.
- **incomplete_details** (object) (required): Details on why the run is incomplete. Will be `null` if the run is not incomplete.
  - **reason** (string (max_completion_tokens|max_prompt_tokens)): The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run. ("max_completion_tokens"|"max_prompt_tokens")
- **model** (string) (required): The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.
- **instructions** (string) (required): The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.
- **tools** (array (object)) (required): The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.
  Array items:
    - **type** (string (code_interpreter)) (required): The type of tool being defined: `code_interpreter` ("code_interpreter")
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

- **usage** (object) (required): Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).
  - **completion_tokens** (integer) (required): Number of completion tokens used over the course of the run.
  - **prompt_tokens** (integer) (required): Number of prompt tokens used over the course of the run.
  - **total_tokens** (integer) (required): Total number of tokens used (prompt + completion).
- **temperature** (number): The sampling temperature used for this run. If not set, defaults to 1.
- **top_p** (number): The nucleus sampling value used for this run. If not set, defaults to 1.
- **max_prompt_tokens** (integer) (required): The maximum number of prompt tokens specified to have been used over the course of the run.

- **max_completion_tokens** (integer) (required): The maximum number of completion tokens specified to have been used over the course of the run.

- **truncation_strategy** (object) (required): Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.
  - **type** (string (auto|last_messages)) (required): The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`. ("auto"|"last_messages")
  - **last_messages** (integer): The number of most recent messages from the thread when constructing the context for the run.
- **tool_choice** (string (none|auto|required)) (required): `none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.
 ("none"|"auto"|"required")
- **parallel_tool_calls** (boolean) (required): Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.
- **response_format** (string (auto)) (required): `auto` is the default value
 ("auto")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}"
```

```

--------------------------------

### POST /organization/projects/{project_id}/certificates/activate

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Activate certificates at the project level.

You can atomically and idempotently activate up to 10 certificates at a time.


```markdown
### Parameters

- **project_id** (string, path, required): The ID of the project.

### Request Body

**Content-Type:** application/json

- **certificate_ids** (array (string)) (required)

### Responses

#### 200 - Certificates activated successfully.

**ListCertificatesResponse**
- **data** (array (object)) (required)
  Array items:
    - **object** (string (certificate|organization.certificate|organization.project.certificate)) (required): The object type.

- If creating, updating, or getting a specific certificate, the object type is `certificate`.
- If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
- If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.
 ("certificate"|"organization.certificate"|"organization.project.certificate")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **name** (string) (required): The name of the certificate.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) of when the certificate was uploaded.
    - **certificate_details** (object) (required)
      - **valid_at** (integer): The Unix timestamp (in seconds) of when the certificate becomes valid.
      - **expires_at** (integer): The Unix timestamp (in seconds) of when the certificate expires.
      - **content** (string): The content of the certificate in PEM format.
    - **active** (boolean): Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.
- **first_id** (string) (example: "cert_abc")
- **last_id** (string) (example: "cert_abc")
- **has_more** (boolean) (required)
- **object** (string (list)) (required) ("list")

### Example Usage

```bash
curl -X POST "https://api.openai.com/v1/organization/projects/{project_id}/certificates/activate" \
  -H "Content-Type: application/json" \
  -d '{
  "certificate_ids": [
    "cert_abc"
  ]
}'
```

```

--------------------------------

### Schema: ListFineTuningCheckpointPermissionResponse

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Schema definition for ListFineTuningCheckpointPermissionResponse

```markdown
## Schema: ListFineTuningCheckpointPermissionResponse

Schema definition for ListFineTuningCheckpointPermissionResponse

**Type:** object

- **data** (array (object)) (required)
  Array items:
    - **id** (string) (required): The permission identifier, which can be referenced in the API endpoints.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the permission was created.
    - **project_id** (string) (required): The project identifier that the permission is for.
    - **object** (string (checkpoint.permission)) (required): The object type, which is always "checkpoint.permission". ("checkpoint.permission")
- **object** (string (list)) (required) ("list")
- **first_id** (string)
- **last_id** (string)
- **has_more** (boolean) (required)

```

--------------------------------

### GET /organization/projects/{project_id}/api_keys

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns a list of API keys in the project.

```markdown
### Parameters

- **project_id** (string, path, required): The ID of the project.
- **limit** (integer, query, optional): A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- **after** (string, query, optional): A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.


### Responses

#### 200 - Project API keys listed successfully.

**ProjectApiKeyListResponse**
- **object** (string (list)) (required) ("list")
- **data** (array (object)) (required)
  Array items:
    - **object** (string (organization.project.api_key)) (required): The object type, which is always `organization.project.api_key` ("organization.project.api_key")
    - **redacted_value** (string) (required): The redacted value of the API key
    - **name** (string) (required): The name of the API key
    - **created_at** (integer) (required): The Unix timestamp (in seconds) of when the API key was created
    - **last_used_at** (integer) (required): The Unix timestamp (in seconds) of when the API key was last used.
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **owner** (object) (required)
      - **type** (string (user|service_account)): `user` or `service_account` ("user"|"service_account")
      - **user** (object): Represents an individual user in a project.
        - **object** (string (organization.project.user)) (required): The object type, which is always `organization.project.user` ("organization.project.user")
        - **id** (string) (required): The identifier, which can be referenced in API endpoints
        - **name** (string) (required): The name of the user
        - **email** (string) (required): The email address of the user
        - **role** (string (owner|member)) (required): `owner` or `member` ("owner"|"member")
        - **added_at** (integer) (required): The Unix timestamp (in seconds) of when the project was added.
      - **service_account** (object): Represents an individual service account in a project.
        - **object** (string (organization.project.service_account)) (required): The object type, which is always `organization.project.service_account` ("organization.project.service_account")
        - **id** (string) (required): The identifier, which can be referenced in API endpoints
        - **name** (string) (required): The name of the service account
        - **role** (string (owner|member)) (required): `owner` or `member` ("owner"|"member")
        - **created_at** (integer) (required): The Unix timestamp (in seconds) of when the service account was created
- **first_id** (string) (required)
- **last_id** (string) (required)
- **has_more** (boolean) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/projects/{project_id}/api_keys?limit=20&after=string"
```

```

--------------------------------

### GET /organization/projects/{project_id}/users/{user_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves a user in the project.

```markdown
### Parameters

- **project_id** (string, path, required): The ID of the project.
- **user_id** (string, path, required): The ID of the user.

### Responses

#### 200 - Project user retrieved successfully.

**ProjectUser**
- **object** (string (organization.project.user)) (required): The object type, which is always `organization.project.user` ("organization.project.user")
- **id** (string) (required): The identifier, which can be referenced in API endpoints
- **name** (string) (required): The name of the user
- **email** (string) (required): The email address of the user
- **role** (string (owner|member)) (required): `owner` or `member` ("owner"|"member")
- **added_at** (integer) (required): The Unix timestamp (in seconds) of when the project was added.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/projects/{project_id}/users/{user_id}"
```

```

--------------------------------

### GET /threads/{thread_id}/messages/{message_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieve a message.

```markdown
### Parameters

- **thread_id** (string, path, required): The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) to which this message belongs.
- **message_id** (string, path, required): The ID of the message to retrieve.

### Responses

#### 200 - OK

**MessageObject**
- **id** (string) (required): The identifier, which can be referenced in API endpoints.
- **object** (string (thread.message)) (required): The object type, which is always `thread.message`. ("thread.message")
- **created_at** (integer) (required): The Unix timestamp (in seconds) for when the message was created.
- **thread_id** (string) (required): The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.
- **status** (string (in_progress|incomplete|completed)) (required): The status of the message, which can be either `in_progress`, `incomplete`, or `completed`. ("in_progress"|"incomplete"|"completed")
- **incomplete_details** (object) (required): On an incomplete message, details about why the message is incomplete.
  - **reason** (string (content_filter|max_tokens|run_cancelled|run_expired|run_failed)) (required): The reason the message is incomplete. ("content_filter"|"max_tokens"|"run_cancelled"|"run_expired"|"run_failed")
- **completed_at** (integer) (required): The Unix timestamp (in seconds) for when the message was completed.
- **incomplete_at** (integer) (required): The Unix timestamp (in seconds) for when the message was marked as incomplete.
- **role** (string (user|assistant)) (required): The entity that produced the message. One of `user` or `assistant`. ("user"|"assistant")
- **content** (array (object)) (required): The content of the message in array of text and/or images.
  Array items:
    - **type** (string (image_file)) (required): Always `image_file`. ("image_file")
    - **image_file** (object) (required)
      - **file_id** (string) (required): The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.
      - **detail** (string (auto|low|high)): Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`. ("auto"|"low"|"high")
- **assistant_id** (string) (required): If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.
- **run_id** (string) (required): The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.
- **attachments** (array (object)) (required): A list of files attached to the message, and the tools they were added to.
  Array items:
    - **file_id** (string): The ID of the file to attach to the message.
    - **tools** (array (object)): The tools to add this file to.
      Array items:
        - **type** (string (code_interpreter)) (required): The type of tool being defined: `code_interpreter` ("code_interpreter")
- **metadata** (object) (required): Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}"
```

```

--------------------------------

### GET /containers/{container_id}/files/{file_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieve Container File

```markdown
### Parameters

- **container_id** (string, path, required)
- **file_id** (string, path, required)

### Responses

#### 200 - Success

**ContainerFileResource**
- **id** (string) (required): Unique identifier for the file.
- **object** (string) (required): The type of this object (`container.file`).
- **container_id** (string) (required): The container this file belongs to.
- **created_at** (integer) (required): Unix timestamp (in seconds) when the file was created.
- **bytes** (integer) (required): Size of the file in bytes.
- **path** (string) (required): Path of the file in the container.
- **source** (string) (required): Source of the file (e.g., `user`, `assistant`).

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/containers/{container_id}/files/{file_id}"
```

```

--------------------------------

### Schema: Function tool call

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

A tool call to run a function. See the 
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.


```markdown
## Schema: Function tool call

A tool call to run a function. See the 
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.


**Type:** object

- **id** (string): The unique ID of the function tool call.

- **type** (string (function_call)) (required): The type of the function tool call. Always `function_call`.
 ("function_call")
- **call_id** (string) (required): The unique ID of the function tool call generated by the model.

- **name** (string) (required): The name of the function to run.

- **arguments** (string) (required): A JSON string of the arguments to pass to the function.

- **status** (string (in_progress|completed|incomplete)): The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.
 ("in_progress"|"completed"|"incomplete")

```

--------------------------------

### GET /files/{file_id}/content

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returns the contents of the specified file.

```markdown
### Parameters

- **file_id** (string, path, required): The ID of the file to use for this request.

### Responses

#### 200 - OK


### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/files/{file_id}/content"
```

```

--------------------------------

### GET /chatkit/threads/{thread_id}/items

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List ChatKit thread items

```markdown
### Parameters

- **thread_id** (string, path, required): Identifier of the ChatKit thread whose items are requested. (example: "cthr_123")
- **limit** (integer, query, optional): Maximum number of thread items to return. Defaults to 20.
- **order** (OrderEnum, query, optional): Sort order for results by creation time. Defaults to `desc`.
- **after** (string, query, optional): List items created after this thread item ID. Defaults to null for the first page.
- **before** (string, query, optional): List items created before this thread item ID. Defaults to null for the newest results.

### Responses

#### 200 - Success

**ThreadItemListResource**
- **object** (unknown) (required): The type of object returned, must be `list`.
- **data** (array (object)) (required): A list of items
  Array items:
    - **id** (string) (required): Identifier of the thread item.
    - **object** (string (chatkit.thread_item)) (required): Type discriminator that is always `chatkit.thread_item`. ("chatkit.thread_item")
    - **created_at** (integer) (required): Unix timestamp (in seconds) for when the item was created.
    - **thread_id** (string) (required): Identifier of the parent thread.
    - **type** (string (chatkit.user_message)) (required) ("chatkit.user_message")
    - **content** (array (object)) (required): Ordered content elements supplied by the user.
      Array items:
        - **type** (string (input_text)) (required): Type discriminator that is always `input_text`. ("input_text")
        - **text** (string) (required): Plain-text content supplied by the user.
    - **attachments** (array (object)) (required): Attachments associated with the user message. Defaults to an empty list.
      Array items:
        - **type** (string (image|file)) (required) ("image"|"file")
        - **id** (string) (required): Identifier for the attachment.
        - **name** (string) (required): Original display name for the attachment.
        - **mime_type** (string) (required): MIME type of the attachment.
        - **preview_url** (string) (required): Preview URL for rendering the attachment inline.
    - **inference_options** (object) (required): Model and tool overrides applied when generating the assistant response.
      - **tool_choice** (object) (required): Tool selection that the assistant should honor when executing the item.
        - **id** (string) (required): Identifier of the requested tool.
      - **model** (string) (required): Model name that generated the response. Defaults to null when using the session default.
- **first_id** (string) (required): The ID of the first item in the list.
- **last_id** (string) (required): The ID of the last item in the list.
- **has_more** (boolean) (required): Whether there are more items available.

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/chatkit/threads/{thread_id}/items?limit=0&order=value&after=string&before=string"
```

```

--------------------------------

### GET /organization/projects/{project_id}/api_keys/{key_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieves an API key in the project.

```markdown
### Parameters

- **project_id** (string, path, required): The ID of the project.
- **key_id** (string, path, required): The ID of the API key.

### Responses

#### 200 - Project API key retrieved successfully.

**ProjectApiKey**
- **object** (string (organization.project.api_key)) (required): The object type, which is always `organization.project.api_key` ("organization.project.api_key")
- **redacted_value** (string) (required): The redacted value of the API key
- **name** (string) (required): The name of the API key
- **created_at** (integer) (required): The Unix timestamp (in seconds) of when the API key was created
- **last_used_at** (integer) (required): The Unix timestamp (in seconds) of when the API key was last used.
- **id** (string) (required): The identifier, which can be referenced in API endpoints
- **owner** (object) (required)
  - **type** (string (user|service_account)): `user` or `service_account` ("user"|"service_account")
  - **user** (object): Represents an individual user in a project.
    - **object** (string (organization.project.user)) (required): The object type, which is always `organization.project.user` ("organization.project.user")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **name** (string) (required): The name of the user
    - **email** (string) (required): The email address of the user
    - **role** (string (owner|member)) (required): `owner` or `member` ("owner"|"member")
    - **added_at** (integer) (required): The Unix timestamp (in seconds) of when the project was added.
  - **service_account** (object): Represents an individual service account in a project.
    - **object** (string (organization.project.service_account)) (required): The object type, which is always `organization.project.service_account` ("organization.project.service_account")
    - **id** (string) (required): The identifier, which can be referenced in API endpoints
    - **name** (string) (required): The name of the service account
    - **role** (string (owner|member)) (required): `owner` or `member` ("owner"|"member")
    - **created_at** (integer) (required): The Unix timestamp (in seconds) of when the service account was created

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/projects/{project_id}/api_keys/{key_id}"
```

```

--------------------------------

### Schema: RealtimeSession

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Realtime session object for the beta interface.

```markdown
## Schema: RealtimeSession

Realtime session object for the beta interface.

**Type:** object

- **id** (string): Unique identifier for the session that looks like `sess_1234567890abcdef`.

- **object** (string (realtime.session)): The object type. Always `realtime.session`. ("realtime.session")
- **modalities** (array): The set of modalities the model can respond with. To disable audio,
set this to ["text"].

- **model** (string (gpt-realtime|gpt-realtime-2025-08-28|gpt-4o-realtime-preview|gpt-4o-realtime-preview-2024-10-01|gpt-4o-realtime-preview-2024-12-17|gpt-4o-realtime-preview-2025-06-03|gpt-4o-mini-realtime-preview|gpt-4o-mini-realtime-preview-2024-12-17|gpt-realtime-mini|gpt-realtime-mini-2025-10-06|gpt-audio-mini|gpt-audio-mini-2025-10-06)): The Realtime model used for this session.
 ("gpt-realtime"|"gpt-realtime-2025-08-28"|"gpt-4o-realtime-preview"|"gpt-4o-realtime-preview-2024-10-01"|"gpt-4o-realtime-preview-2024-12-17"|"gpt-4o-realtime-preview-2025-06-03"|"gpt-4o-mini-realtime-preview"|"gpt-4o-mini-realtime-preview-2024-12-17"|"gpt-realtime-mini"|"gpt-realtime-mini-2025-10-06"|"gpt-audio-mini"|"gpt-audio-mini-2025-10-06")
- **instructions** (string): The default system instructions (i.e. system message) prepended to model
calls. This field allows the client to guide the model on desired
responses. The model can be instructed on response content and format,
(e.g. "be extremely succinct", "act friendly", "here are examples of good
responses") and on audio behavior (e.g. "talk quickly", "inject emotion
into your voice", "laugh frequently"). The instructions are not
guaranteed to be followed by the model, but they provide guidance to the
model on the desired behavior.


Note that the server sets default instructions which will be used if this
field is not set and are visible in the `session.created` event at the
start of the session.

- **voice** (string)
- **input_audio_format** (string (pcm16|g711_ulaw|g711_alaw)): The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`.
For `pcm16`, input audio must be 16-bit PCM at a 24kHz sample rate,
single channel (mono), and little-endian byte order.
 ("pcm16"|"g711_ulaw"|"g711_alaw")
- **output_audio_format** (string (pcm16|g711_ulaw|g711_alaw)): The format of output audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`.
For `pcm16`, output audio is sampled at a rate of 24kHz.
 ("pcm16"|"g711_ulaw"|"g711_alaw")
- **input_audio_transcription** (object)
  - **model** (string (whisper-1|gpt-4o-mini-transcribe|gpt-4o-transcribe|gpt-4o-transcribe-diarize)): The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.
 ("whisper-1"|"gpt-4o-mini-transcribe"|"gpt-4o-transcribe"|"gpt-4o-transcribe-diarize")
  - **language** (string): The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

  - **prompt** (string): An optional text to guide the model's style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://platform.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example "expect words related to technology".

- **turn_detection** (object): Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.
  - **type** (string) (required): Type of turn detection, `server_vad` to turn on simple Server VAD.

  - **threshold** (number): Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

  - **prefix_padding_ms** (integer): Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

  - **silence_duration_ms** (integer): Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

  - **create_response** (boolean): Whether or not to automatically generate a response when a VAD stop event occurs.

  - **interrupt_response** (boolean): Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

  - **idle_timeout_ms** (integer): Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response's audio has finished playing,
i.e. it's set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

- **input_audio_noise_reduction** (object): Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

  - **type** (string (near_field|far_field)): Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.
 ("near_field"|"far_field")
- **speed** (number): The speed of the model's spoken response. 1.0 is the default speed. 0.25 is
the minimum speed. 1.5 is the maximum speed. This value can only be changed
in between model turns, not while a response is in progress.

- **tracing** (string (auto)): Default tracing mode for the session.
 ("auto")
- **tools** (array (object)): Tools (functions) available to the model.
  Array items:
    - **type** (string (function)): The type of the tool, i.e. `function`. ("function")
    - **name** (string): The name of the function.
    - **description** (string): The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

    - **parameters** (object): Parameters of the function in JSON Schema.
- **tool_choice** (string): How the model chooses tools. Options are `auto`, `none`, `required`, or
specify a function.

- **temperature** (number): Sampling temperature for the model, limited to [0.6, 1.2]. For audio models a temperature of 0.8 is highly recommended for best performance.

- **max_response_output_tokens** (integer)
- **expires_at** (integer): Expiration timestamp for the session, in seconds since epoch.
- **prompt** (object): Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

  - **id** (string) (required): The unique identifier of the prompt template to use.
  - **version** (string): Optional version of the prompt template.
  - **variables** (object): Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

- **include** (array (string (item.input_audio_transcription.logprobs))): Additional fields to include in server outputs.
- `item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.


```

--------------------------------

### GET /organization/admin_api_keys/{key_id}

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Retrieve a single organization API key

```markdown
### Parameters

- **key_id** (string, path, required)

### Responses

#### 200 - Details of the requested API key.

**AdminApiKey**
- **object** (string) (required): The object type, which is always `organization.admin_api_key` (example: "organization.admin_api_key")
- **id** (string) (required): The identifier, which can be referenced in API endpoints (example: "key_abc")
- **name** (string) (required): The name of the API key (example: "Administration Key")
- **redacted_value** (string) (required): The redacted value of the API key (example: "sk-admin...def")
- **value** (string): The value of the API key. Only shown on create. (example: "sk-admin-1234abcd")
- **created_at** (integer (int64)) (required): The Unix timestamp (in seconds) of when the API key was created (example: 1711471533)
- **last_used_at** (integer (int64)) (required): The Unix timestamp (in seconds) of when the API key was last used (example: 1711471534)
- **owner** (object) (required)
  - **type** (string): Always `user` (example: "user")
  - **object** (string): The object type, which is always organization.user (example: "organization.user")
  - **id** (string): The identifier, which can be referenced in API endpoints (example: "sa_456")
  - **name** (string): The name of the user (example: "My Service Account")
  - **created_at** (integer (int64)): The Unix timestamp (in seconds) of when the user was created (example: 1711471533)
  - **role** (string): Always `owner` (example: "owner")

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/organization/admin_api_keys/{key_id}"
```

```

--------------------------------

### GET /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

List checkpoints for a fine-tuning job.


```markdown
### Parameters

- **fine_tuning_job_id** (string, path, required): The ID of the fine-tuning job to get checkpoints for.
 (example: "ft-AF1WoRqd3aJAHsqc9NY7iL8F")
- **after** (string, query, optional): Identifier for the last checkpoint ID from the previous pagination request.
- **limit** (integer, query, optional): Number of checkpoints to retrieve.

### Responses

#### 200 - OK

**ListFineTuningJobCheckpointsResponse**
- **data** (array (object)) (required)
  Array items:
    - **id** (string) (required): The checkpoint identifier, which can be referenced in the API endpoints.
    - **created_at** (integer) (required): The Unix timestamp (in seconds) for when the checkpoint was created.
    - **fine_tuned_model_checkpoint** (string) (required): The name of the fine-tuned checkpoint model that is created.
    - **step_number** (integer) (required): The step number that the checkpoint was created at.
    - **metrics** (object) (required): Metrics at the step number during the fine-tuning job.
      - **step** (number)
      - **train_loss** (number)
      - **train_mean_token_accuracy** (number)
      - **valid_loss** (number)
      - **valid_mean_token_accuracy** (number)
      - **full_valid_loss** (number)
      - **full_valid_mean_token_accuracy** (number)
    - **fine_tuning_job_id** (string) (required): The name of the fine-tuning job that this checkpoint was created from.
    - **object** (string (fine_tuning.job.checkpoint)) (required): The object type, which is always "fine_tuning.job.checkpoint". ("fine_tuning.job.checkpoint")
- **object** (string (list)) (required) ("list")
- **first_id** (string)
- **last_id** (string)
- **has_more** (boolean) (required)

### Example Usage

```bash
curl -X GET "https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints?after=string&limit=10"
```

```

--------------------------------

### Schema: RealtimeBetaServerEventMCPListToolsInProgress

Source: https://app.stainless.com/api/spec/documented/openai/openapi.documented.yml

Returned when listing MCP tools is in progress for an item.

```markdown
## Schema: RealtimeBetaServerEventMCPListToolsInProgress

Returned when listing MCP tools is in progress for an item.

**Type:** object

- **event_id** (string) (required): The unique ID of the server event.
- **type** (unknown) (required): The event type, must be `mcp_list_tools.in_progress`.
- **item_id** (string) (required): The ID of the MCP list tools item.

```