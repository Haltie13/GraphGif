import os
from parsing import parse_graphgif_file
from visitors import GraphgifPrettyPrinter, GraphStatisticsVisitor
from algorithms import AlgorithmExecutor

example_dir = '../examples'
executor = AlgorithmExecutor()

for example_file in os.listdir(example_dir):
    example_path = os.path.join(example_dir, example_file)
    print('\n' + '-' * 10 + f' EXAMPLE: {example_file} ' + '-' * 10)

    try:
        ast, graph_model = parse_graphgif_file(example_path)

        # Algorithm analysis
        print("\nAlgorithm Compatibility:")
        print("=" * 40)

        compatible_algorithms = executor.get_algorithms_for_graph(graph_model)
        for alg_name, info in compatible_algorithms.items():
            status = "✅" if info['valid'] else "❌"
            print(f"{status} {info['name']} ({info['type']})")
            if not info['valid']:
                print(f"   Reason: {info['reason']}")

        # Execute a compatible algorithm
        for alg_name, info in compatible_algorithms.items():
            if info['valid']:
                print(f"\nExecuting {info['name']}:")
                result = executor.execute_algorithm(alg_name, graph_model)

                if result.success:
                    print(f"  Steps: {len(result.states)}")
                    print(f"  Execution time: {result.execution_time:.4f}s")
                    print(f"  Result: {result.final_result}")

                    # Show first few states
                    for i, state in enumerate(result.states[:3]):
                        print(f"  Step {state.step}: {state.description}")
                else:
                    print(f"  Error: {result.error_message}")
                break

    except Exception as e:
        print(f"Error processing {example_file}: {e}")