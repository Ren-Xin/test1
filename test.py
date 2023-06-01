# Import Steamship
from steamship import Steamship

# Load a user-contributed package
api = Steamship.use('keyword-generator')

# Add AI to your app with a single line
keywords = api.invoke('generate', text=MY_ARTICLE)
# Create a Steamship client
# NOTE: When developing a package, just use `self.client`
client = Steamship(workspace="gpt-4")

# Create an instance of this generator
generator = client.use_plugin('gpt-4')
# Generate text
task = generator.generate(text="This is your prompt text")

# Wait for completion of the task.
task.wait()

# Print the output
print(task.output.blocks[0].text)
