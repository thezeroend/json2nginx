from infrastructure.reader import load_json_configs
from infrastructure.validator import validate_routes
from infrastructure.generator import generate_location_blocks
import os
import sys

def main(configs_dir, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)

        configs_por_arquivo = load_json_configs(configs_dir)
        validate_routes(configs_por_arquivo)

        for filename, config_data in configs_por_arquivo.items():
            result = generate_location_blocks(config_data)
            print(result)
            output_filename = os.path.splitext(filename)[0] + ".conf"
            output_path = os.path.join(output_dir, output_filename)

            with open(output_path, "w") as f:
                f.write(result)

            print(f"✅ Gerado: {output_path}")

    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
