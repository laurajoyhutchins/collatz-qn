\
.PHONY: all data counts fit plots unpack verify clean-unpacked clean

ZIP := data/raw/qn_exponents_package.zip
UNPACK_DIR := data/raw/unpacked

all: counts fit plots

## Unzip raw package into a git-ignored folder
unpack: $(ZIP)
	@mkdir -p $(UNPACK_DIR)
	@command -v unzip >/dev/null 2>&1 || { echo "unzip not found"; exit 1; }
	unzip -o -q "$(ZIP)" -d "$(UNPACK_DIR)"
	@echo "Unpacked to $(UNPACK_DIR)"

## Verify ZIP integrity (optional)
verify: $(ZIP)
	@shasum -a 256 -c data/raw/qn_exponents_package.sha256

data:
	@python -m scripts.compute_counts

counts:
	@python -m scripts.compute_counts

fit:
	@python -m scripts.fit_zipf_models

plots:
	@python -m scripts.plot_figures

clean-unpacked:
	@rm -rf "$(UNPACK_DIR)"

clean:
	@rm -rf data/processed/*.csv figures/*.png results/*
