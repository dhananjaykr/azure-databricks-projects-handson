from file_processor import write_report


def test_write_report(tmp_path):
    output_file = tmp_path / "report.txt"
    write_report(output_file, "Pipeline completed")

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == "Pipeline completed"
